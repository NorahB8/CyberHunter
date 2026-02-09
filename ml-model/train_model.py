"""
CyberHunter ML Model Training
Trains a Random Forest classifier on real phishing examples
"""

import re
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from training_data import TRAINING_DATA, get_stats
from feature_extractor import FeatureExtractor



def train_model():
    """Train Random Forest classifier on phishing data"""

    print("=" * 80)
    print("CyberHunter ML Model Training")
    print("=" * 80)

    # Load training data
    stats = get_stats()
    print(f"\nTraining Data:")
    print(f"  Total samples: {stats['total']}")
    print(f"  Phishing: {stats['phishing']}")
    print(f"  Legitimate: {stats['legitimate']}")
    print(f"  Balance: {stats['balance']}")

    # Extract features
    print("\nExtracting features...")
    extractor = FeatureExtractor()

    X = []
    y = []

    for email_data in TRAINING_DATA:
        features = extractor.extract_features(email_data)
        X.append(list(features.values()))
        y.append(email_data['label'])

    X = np.array(X)
    y = np.array(y)

    feature_names = list(extractor.extract_features(TRAINING_DATA[0]).keys())
    print(f"  Extracted {len(feature_names)} features")
    print(f"  Feature names: {', '.join(feature_names[:5])}... (+{len(feature_names)-5} more)")

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    print(f"\nData split:")
    print(f"  Training: {len(X_train)} samples")
    print(f"  Testing: {len(X_test)} samples")

    # Train Random Forest
    print("\nTraining Random Forest Classifier...")
    model = RandomForestClassifier(
        n_estimators=100,      # 100 decision trees
        max_depth=10,          # Prevent overfitting
        min_samples_split=2,
        min_samples_leaf=1,
        random_state=42
    )

    model.fit(X_train, y_train)
    print("  Training complete!")

    # Evaluate on test set
    print("\n" + "=" * 80)
    print("Model Evaluation")
    print("=" * 80)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print(f"\nTest Set Accuracy: {accuracy * 100:.2f}%")

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred,
                               target_names=['Legitimate', 'Phishing'],
                               digits=3))

    print("Confusion Matrix:")
    cm = confusion_matrix(y_test, y_pred)
    print(f"                Predicted")
    print(f"                Legit  Phishing")
    print(f"Actual Legit      {cm[0][0]:3d}      {cm[0][1]:3d}")
    print(f"       Phishing   {cm[1][0]:3d}      {cm[1][1]:3d}")

    # Cross-validation
    print("\nCross-Validation (5-fold):")
    cv_scores = cross_val_score(model, X, y, cv=5)
    print(f"  CV Scores: {cv_scores}")
    print(f"  Mean CV Accuracy: {cv_scores.mean() * 100:.2f}% (+/- {cv_scores.std() * 2 * 100:.2f}%)")

    # Feature importance
    print("\nTop 10 Most Important Features:")
    feature_importance = sorted(
        zip(feature_names, model.feature_importances_),
        key=lambda x: x[1],
        reverse=True
    )
    for i, (feature, importance) in enumerate(feature_importance[:10], 1):
        print(f"  {i:2d}. {feature:30s} {importance:.4f}")

    # Save model
    print("\nSaving model...")
    model_data = {
        'model': model,
        'feature_extractor': extractor,
        'feature_names': feature_names,
        'accuracy': accuracy,
        'cv_score': cv_scores.mean()
    }

    with open('cyberhunter_ml_model.pkl', 'wb') as f:
        pickle.dump(model_data, f)

    print("  Model saved to: cyberhunter_ml_model.pkl")

    print("\n" + "=" * 80)
    print("Training Complete!")
    print("=" * 80)

    return model, extractor, feature_names


if __name__ == '__main__':
    train_model()
