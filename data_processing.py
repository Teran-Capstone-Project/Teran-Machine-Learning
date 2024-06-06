import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Membaca dataset
file_path = 'Student Mental health.csv'
data = pd.read_csv(file_path)

# Menampilkan beberapa baris pertama dari dataset
print("Data sebelum preprocessing:")
print(data.head())

# Melakukan label encoding pada kolom kategorikal
label_encoders = {}
for column in data.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le

# Menampilkan beberapa baris pertama dari dataset setelah label encoding
print("\nData setelah label encoding:")
print(data.head())

# Memisahkan fitur dan label
# Asumsikan bahwa kolom terakhir adalah label
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Membagi data menjadi set pelatihan dan pengujian
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Menampilkan ukuran dari set pelatihan dan pengujian
print("\nUkuran set pelatihan dan pengujian:")
print(f"X_train: {X_train.shape}")
print(f"X_test: {X_test.shape}")
print(f"y_train: {y_train.shape}")
print(f"y_test: {y_test.shape}")