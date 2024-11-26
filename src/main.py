# -*- coding: utf-8 -*-
"""Main.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MVSXiuuIWudXFJvay3xzhZvmf14Q83Pz

## 1.Data Preparation
"""

#import library yang dibutuhkan
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

#load dataset
df = pd.read_csv("../data/Crop_recommendation.csv")

#melihat 5 baris data awal
df.head()

print(f'Peneliti mempunyai {df.shape[0]} baris dan {df.shape[1]} kolom')

# membuat function untuk melihat informasi lebih mendalam
def inspect_dataframe(df):
    print(f'The dataframe contains {df.shape[0]} rows and {df.shape[1]} cols.')
    print(f"- {len(df.select_dtypes(include='number').columns)} are numeric cols")
    print(f"- {len(df.select_dtypes(include='O').columns)} are object cols")
    summary = {
        'ColumnName': df.columns.values.tolist(),
        'Nrow': df.shape[0],
        'DataType': df.dtypes.values.tolist(),
        'NAPct': (df.isna().mean() * 100).round(2).tolist(),
        'DuplicatePct': (df.duplicated().sum()/len(df)*100).round(2),
        'UniqueValue': df.nunique().tolist(),
        'Sample': [df[col].unique() for col in df.columns]
    }
    return pd.DataFrame(summary)

inspect_dataframe(df)

"""1. pada dataset mempunyai 3 kolom bertipe int, 4 kolom float dan 1 object.
2. sejauh ini data yang kita punya sesuai dengan type masing-masing data inputnya.
3. terdapat indikasi bahwa ada sekitar 6% data duplicated.
"""

display(df.describe(), df.describe(include='object'))

"""1. peneliti melihat adanya data yang rangenya sangat lebar pada kolom N,P dan K.
2. peneliti melihat pada kolom N dengan nilai minim 0 apakah ini data yang valid atau tidak akan saya telusuri lebih lanjut.
"""

# Plot distribusi data untuk setiap kolom numerik
numerical_columns = df.select_dtypes(include=['number']).columns

for col in numerical_columns:
    plt.figure(figsize=(10, 5))
    sns.histplot(df[col], kde=True, color='blue')
    plt.title(f"Distribusi Kolom {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.show()

# define kolom yang bertujuan melihat distribusi dari masing-masing kolom numeric
numerical_columns = df.select_dtypes(include='number')

# setup up figure size
plt.figure(figsize=(15, 7), dpi=200)
plt.suptitle('Distribution of Numerical Features', fontsize=18)

# check outliers using boxplots
for i, col in enumerate(numerical_columns):
    plt.subplot(5, 3, i+1)
    sns.boxplot(x=df[col], color='cornflowerblue', orient='v')
    plt.title(f'{col}')
    plt.xlabel(None)

plt.tight_layout()
plt.show()

"""1. pada kolom N tidak ada data yang outlier tetapi dri boxplotnya mungkin terindikasi dia right skewed.
2. pada kolom P terdapat nilai outlier yang banyak.
3. pada kolom K ini terdapat beberapa nilai yang sangat tinggi.
4. pada kolom temparatur mungkin ini wajar dikarenakan bisa saja temparatur sangat berubah ubah pada suatu kondisi tertentu.
5. pada kolom humidity tidak terdapat outliyer yang tinggi tapi dariboxplotnya mungin ini ada indikasi left skewed.
6. pada kolom ph  dan rainfall juga terdapat outlier.

### 1.Cek Missing value
"""

# cek missing value
df.isna().sum().to_frame().reset_index().rename(columns={"index":"column_name", 0:"value"})

"""pada kasus kali ini dataset tidak memiliki data yang null.

### 2.Cek Duplicated
"""

#cek duplicated
df[df.duplicated()]

"""pada dataset mempunyai data duplicated sebanyak 103 baris, langkah kedepanya peneliti akan menghapus data duplicated ini."""

#kita ambil data yang pertama pada data duplicated
df = df.drop_duplicates(keep='first')

display(df.head(len(df)), df[df.duplicated()])

"""### 3.Cek Outlier"""

# define kolom yang bertujuan melihat distribusi dari masing-masing kolom numeric
numerical_columns = df.select_dtypes(include='number')

# setup up figure size
plt.figure(figsize=(15, 7), dpi=200)
plt.suptitle('Distribution of Numerical Features', fontsize=18)

# check outliers using boxplots
for i, col in enumerate(numerical_columns):
    plt.subplot(5, 3, i+1)
    sns.boxplot(x=df[col], color='cornflowerblue', orient='v')
    plt.title(f'{col}')
    plt.xlabel(None)

plt.tight_layout()
plt.show()

# Identifikasi kolom numerik
numerical_columns = df.select_dtypes(include=['number']).columns

# Loop untuk mengecek outlier di setiap kolom numerik
for column in numerical_columns:
    Q1 = df[column].quantile(0.25)  # Kuartil pertama
    Q3 = df[column].quantile(0.75)  # Kuartil ketiga
    IQR = Q3 - Q1  # Rentang antar-kuartil

    lower = Q1 - 1.5 * IQR  # Batas bawah
    upper = Q3 + 1.5 * IQR  # Batas atas

    # Identifikasi nilai outlier
    outliers = df[(df[column] < lower) | (df[column] > upper)]
    print(f"Kolom: {column}")
    print(f"Jumlah outlier: {len(outliers)}")
    print(outliers[[column]])  # Menampilkan data outlier untuk kolom tersebut
    print("-" * 50)

"""1. peneliti mendapatkan beberapa kolom yang memiliki banyak outlier tetapi hall ini wajar karna unsur tanah yang alami memang memiliki unser yang berbeda.
2. peneliti tidak akan melakukan drop atau penghapusan data outlier ini dikarenakan data yang diberikan sangat penting.

## 2.Exploratory Data Analysis(EDA)

### 1.Univariate analyst
"""

df.head(100)

# Visualisasi data
plt.figure(figsize=(15, 8))
ax = sns.countplot(data=df, x="label", palette="magma")

# Tambahkan angka di atas setiap bar
for container in ax.containers:
    ax.bar_label(container, fmt='%d', label_type='edge', fontsize=12, padding=3)

# Tambahkan judul dan label
plt.title("Distribusi Label Target", fontsize=18, weight='bold')
plt.xlabel("Tumbuhan", fontsize=14)
plt.ylabel("Jumlah", fontsize=14)

# Tata letak agar tidak berantakan
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout(pad=-1)
plt.show()

"""1. Bisa kita lihat pada dataset distiribusi dari semua kelas label bisa dibilang imbang rangenya tidak terlalu jauh tau imbalance.
2. Bisa dilihat juga kelas yang mendominasi yaitu kelas rise, soyabens dan maize yang lain sama.

#### 2.Bivariate Analyst

##### 1. Target dengan Nitrogen(N)
"""

#plot kolom Nitrogen dengan target
plt.figure(figsize=(12, 6))
sns.stripplot(data=df, x="label", y='N', palette="husl", alpha=0.7)
plt.title(f"Strip Plot: Nitrogen vs Label", fontsize=16, weight='bold')
plt.xlabel("Tumbuhan", fontsize=14)
plt.ylabel('Nitrogen', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

"""pada visualisasi diatas kita dapat informasi tentang tumbuhan dengan rata-rata unsur nitrogen pada range 0 sampai 40 dengan tumbuhan tertentu, ada juga yang nilai nitrogenya tinggi seperti cotton dan coffe yang berada disekitaran 100 sampai 140 sedangakan coffe 80 samapai 120 dan masih ada banana dan watermelon yanbg berada pada 80 hingga 120.

##### 2. Target dengan Fosfor(P)
"""

#plot kolom fosfor dengan target
plt.figure(figsize=(12, 6))
sns.stripplot(data=df, x="label", y='P', palette="husl", alpha=0.7)
plt.title(f"Strip Plot: Fosfor vs Label", fontsize=16, weight='bold')
plt.xlabel("Tumbuhan", fontsize=14)
plt.ylabel('Fosfor', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

"""pada hasil visualisasi diatas bahwa kita dapat informasi bahwa kadar fosfor untuk setiap tumbuhan itu berbeda, ada yang kebutuhan fosfornya begitu tinggi dari pada yang lainya yaitu tumbuhan grapes dan apple disekitaran 120 hingga 145.

##### 3. Target dengan Kalium(K)
"""

#plot kolom fosfor dengan target
plt.figure(figsize=(12, 6))
sns.stripplot(data=df, x="label", y='K', palette="husl", alpha=0.7)
plt.title(f"Strip Plot: Kalium vs Label", fontsize=16, weight='bold')
plt.xlabel("Tumbuhan", fontsize=14)
plt.ylabel('Kalium', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

"""pada hasil visualisasi diatas kita dapat informasi bahwa grape dan apple itu membutuhkan nilai kalium yang tinggi dibandingakan dengan yang lainya yaitu sekitar 200 lebih.

##### 4. Target dengan Temparature
"""

#plot kolom fosfor dengan target
plt.figure(figsize=(12, 6))
sns.stripplot(data=df, x="label", y='temperature', palette="husl", alpha=0.7)
plt.title(f"Strip Plot: Temparature vs Label", fontsize=16, weight='bold')
plt.xlabel("Tumbuhan", fontsize=14)
plt.ylabel('Temparatur', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

"""pada hasil visualisasi diatas kita dapat informasi bahwasanya grape dan orange memiliki range temparature yang sangat rendah tapi bisa juga sangat extrem diangka 10 hingga 40.

##### 5. Target dengan Humidity
"""

#plot kolom humidity dengan target
plt.figure(figsize=(12, 6))
sns.stripplot(data=df, x="label", y='humidity', palette="husl", alpha=0.7)
plt.title(f"Strip Plot: Humidity vs Label", fontsize=16, weight='bold')
plt.xlabel("Tumbuhan", fontsize=14)
plt.ylabel('Humidity', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

"""pada hasil visualisasi diatas kita dapat informasi bahwa setiap tumbuhan memiliki tingkat kelembapanya masing-masing pada tumbuhan seperti rice dan grape memiliki range yang kecil yang dimana tumbuhan ini hanya akan maksimal bertumbuh pada kelembapan 80-88.

##### 6. Target dengan Ph
"""

#plot kolom humidity dengan target
plt.figure(figsize=(12, 6))
sns.stripplot(data=df, x="label", y='ph', palette="husl", alpha=0.7)
plt.title(f"Strip Plot: Ph vs Label", fontsize=16, weight='bold')
plt.xlabel("Tumbuhan", fontsize=14)
plt.ylabel('Ph', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

"""pada hasil visualisasi diatas kita dapat informasi bahwa yang meiliki ph tinggi yaitu groundnuts yang dimana kita ketahui ph semakin tinggi akan semakin asam, teruntuk tumubhan lain masih pada disekitran 6 dampai 8.

##### 7. Target dengan Rainfall
"""

#plot kolom humidity dengan target
plt.figure(figsize=(12, 6))
sns.stripplot(data=df, x="label", y='rainfall', palette="husl", alpha=0.7)
plt.title(f"Strip Plot: Rainfall vs Label", fontsize=16, weight='bold')
plt.xlabel("Tumbuhan", fontsize=14)
plt.ylabel('Rainfall', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

"""pada hasil visualisasi diatas ternyata untuk tumbuhan rice memiliki curah hujan yanjg sangat tinggi untuk mendapatkan hasil panen yang maksimal, tapi terkadang juga memiliki curah hujan yang kecil, hall ini terjadi karena faktor dari peralihan musim hujan ke panas.

### Insight keseluruhan
1. Pada kebutuhan rata-rata kebutuhan nitrogen pada tumbuhan yaitu sekitar 20-200ppm (sumber chat-gpt4) yang dimana kita lihat pada dataset yang kita punya memang pada range tersebut.
2. Pada kebutuhan fosfor rata-rata penggunaan pada tumbuhan sekitar 10-80ppm (sumber chst-gpt) yang dimana didataset kita mempunya nilai tumbuhan dengan nilai fosfor yang tinggi yaitu pada tumbuhan grape dan apple.
3. Pada kebutuhan kalium rata-rata penggunaan pada tumbuhan sekitar 50-300 ppm (sumber chat-gpt) yang dimana pada dataset kitamasih banyak tumbuhan yang dibawah standar kalium bagi tumbuhan.
4. Pada kebutuhan ph tanah yang baik ada pada sekitaran 6-7 dimana ketika ph semakin tinggi maka tinggkat keasaaman dari tanah akan semakin tinggi.
5. Pada kebutuhan temparature ada beberapa tumbuhan yang memiliki temparature yang tinggi diatas 30 diantaranya grapes, orange, peas dan manggo.
6. pada kebutuhan humidity pada tumbuhan yang kelembabanya lebih dari 90% yaitu apple dan orange.
7. sedangkan tumbuhan dengan rainfall yang tinggi dibutuhkan oleh tumbuhan rice diangka sekitaran 200-300.

#### 3.Multivariate Analyst
"""

# Heatmap korelasi untuk kolom numerik
correlation = df[numerical_columns].corr()
plt.figure(figsize=(12, 10))
sns.heatmap(correlation, annot=True, fmt=".2f", cmap="viridis", cbar=True)
plt.title("Heatmap Korelasi Antar Kolom Numerik")
plt.show()

"""1. Pada hasil visualisasi diatas dilihat, antara Fosfor(P) dan Kalium(K) memiliki hubungan relasi positif yang kuat sekitar 0.83 atau kata lain ketika nilai dari P naik maka variabel K juga naik sebaliknya juga, mungkin bisa saja ketika kebutuhan fosfor dari suatu tumbuhan maka kita juga akan menaikan nilai dari kaliumnya juga.
2. Di kenaikan tingkat kalium juga dipengaruhi oleh tingkat humidity yang sekitar 0.22 yang dimana ini korelasi positive.
3. Berbanding kebalik bagi tingkat Ph yang memiliki korelasi negative sekitaran -0.24 yang artinya ketika Ph semakin tinggi maka tingkat fosfornya semkain dikurangi ataupun sebaliknya.
"""

#save dataset yang sudah dicleaning
df.to_csv('../data/dataset_cleaned.csv', index=False)

"""## 3.Feature Engineering

### 1.Data Spliting
"""

from sklearn.preprocessing import RobustScaler,OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report,f1_score,ConfusionMatrixDisplay
from sklearn.pipeline import Pipeline,make_pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import learning_curve
import joblib

df_new = df.copy()

df_new

X = df_new.drop(['label'], axis=1)
y = df_new['label']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)
X_train.shape, X_test.shape, y_train.shape, y_test.shape

numerical_cols = X.select_dtypes(include=['int', 'float']).columns
categorical_cols = X.select_dtypes(include=['object']).columns

#membuat pipeline untuk tipe Categorical
cat_pipeline = Pipeline([
    ("inpute", SimpleImputer(strategy='most_frequent')),
    ('one-hot' , OneHotEncoder(handle_unknown='ignore', sparse_output= False))
])

#membuat pipeline untuk Numerical
num_pipeline = Pipeline([
    ("inpute", SimpleImputer(strategy='median')),
    ('scaling' , RobustScaler())
])

col_tranform = ColumnTransformer([
    ('cat_transform',cat_pipeline, categorical_cols),
    ('num_transform',num_pipeline, numerical_cols)
], remainder = 'passthrough', n_jobs= -1)

"""## 4.Modeling

### 1.KNN
"""

model_knn = KNeighborsClassifier(n_neighbors = 5)

final_pipeline_knn = make_pipeline(col_tranform, model_knn)

final_pipeline_knn.fit(X_train, y_train)

# Evaluasi pada data latih
y_train_pred = final_pipeline_knn.predict(X_train)
train_f1 = f1_score(y_train, y_train_pred, average="weighted")

# Evaluasi pada data uji
y_test_pred = final_pipeline_knn.predict(X_test)
test_f1 = f1_score(y_test, y_test_pred, average="weighted")

# Print hasil F1 Score
print(f"Train F1 Score: {train_f1:.2f}")
print(f"Test F1 Score: {test_f1:.2f}")

# Analisis Overfitting/Underfitting
if train_f1 > test_f1 + 0.1:
    print("Model kemungkinan overfitting.")
elif train_f1 < 0.7 and test_f1 < 0.7:
    print("Model kemungkinan underfitting.")
else:
    print("Model memiliki generalisasi yang baik.")

# Learning curve dengan F1 Score
train_sizes, train_scores, test_scores = learning_curve(
    final_pipeline_knn, X_train, y_train, cv=5, scoring='f1_weighted', train_sizes=np.linspace(0.1, 1.0, 10)
)

# Rata-rata dan standar deviasi
train_mean = train_scores.mean(axis=1)
train_std = train_scores.std(axis=1)
test_mean = test_scores.mean(axis=1)
test_std = test_scores.std(axis=1)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(train_sizes, train_mean, label='Training F1 Score', color='blue')
plt.plot(train_sizes, test_mean, label='Validation F1 Score', color='orange')

# Error bands
plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, color='blue', alpha=0.2)
plt.fill_between(train_sizes, test_mean - test_std, test_mean + test_std, color='orange', alpha=0.2)

# Labels and Title
plt.title('Learning Curve (F1 Score)', fontsize=16)
plt.xlabel('Training Set Size', fontsize=12)
plt.ylabel('F1 Score', fontsize=12)
plt.legend(loc='best')
plt.grid()
plt.show()

"""### 2.Logistic Regression"""

model_logistic = LogisticRegression()

final_pipeline_logistic = make_pipeline(col_tranform, model_logistic)

final_pipeline_logistic.fit(X_train, y_train)

final_pipeline_logistic.score(X_test, y_test)

# Evaluasi pada data latih
y_train_pred = final_pipeline_logistic.predict(X_train)
train_f1 = f1_score(y_train, y_train_pred, average="weighted")

# Evaluasi pada data uji
y_test_pred = final_pipeline_logistic.predict(X_test)
test_f1 = f1_score(y_test, y_test_pred, average="weighted")

# Print hasil F1 Score
print(f"Train F1 Score: {train_f1:.2f}")
print(f"Test F1 Score: {test_f1:.2f}")

# Analisis Overfitting/Underfitting
if train_f1 > test_f1 + 0.1:
    print("Model kemungkinan overfitting.")
elif train_f1 < 0.7 and test_f1 < 0.7:
    print("Model kemungkinan underfitting.")
else:
    print("Model memiliki generalisasi yang baik.")

# Learning curve dengan F1 Score
train_sizes, train_scores, test_scores = learning_curve(
    final_pipeline_logistic, X_train, y_train, cv=5, scoring='f1_weighted', train_sizes=np.linspace(0.1, 1.0, 10)
)

# Rata-rata dan standar deviasi
train_mean = train_scores.mean(axis=1)
train_std = train_scores.std(axis=1)
test_mean = test_scores.mean(axis=1)
test_std = test_scores.std(axis=1)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(train_sizes, train_mean, label='Training F1 Score', color='blue')
plt.plot(train_sizes, test_mean, label='Validation F1 Score', color='orange')

# Error bands
plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, color='blue', alpha=0.2)
plt.fill_between(train_sizes, test_mean - test_std, test_mean + test_std, color='orange', alpha=0.2)

# Labels and Title
plt.title('Learning Curve (F1 Score)', fontsize=16)
plt.xlabel('Training Set Size', fontsize=12)
plt.ylabel('F1 Score', fontsize=12)
plt.legend(loc='best')
plt.grid()
plt.show()

"""### 3.Suport Vector Machine(SVM)"""

model_svm = SVC(class_weight='balanced')

final_pipeline_svc = make_pipeline(col_tranform, model_svm)

final_pipeline_svc.fit(X_train, y_train)

# Evaluasi pada data latih
y_train_pred = final_pipeline_svc.predict(X_train)
train_f1 = f1_score(y_train, y_train_pred, average="weighted")

# Evaluasi pada data uji
y_test_pred = final_pipeline_svc.predict(X_test)
test_f1 = f1_score(y_test, y_test_pred, average="weighted")

# Print hasil F1 Score
print(f"Train F1 Score: {train_f1:.2f}")
print(f"Test F1 Score: {test_f1:.2f}")

# Analisis Overfitting/Underfitting
if train_f1 > test_f1 + 0.1:
    print("Model kemungkinan overfitting.")
elif train_f1 < 0.7 and test_f1 < 0.7:
    print("Model kemungkinan underfitting.")
else:
    print("Model memiliki generalisasi yang baik.")

# Learning curve dengan F1 Score
train_sizes, train_scores, test_scores = learning_curve(
    final_pipeline_svc, X_train, y_train, cv=5, scoring='f1_weighted', train_sizes=np.linspace(0.1, 1.0, 10)
)

# Rata-rata dan standar deviasi
train_mean = train_scores.mean(axis=1)
train_std = train_scores.std(axis=1)
test_mean = test_scores.mean(axis=1)
test_std = test_scores.std(axis=1)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(train_sizes, train_mean, label='Training F1 Score', color='blue')
plt.plot(train_sizes, test_mean, label='Validation F1 Score', color='orange')

# Error bands
plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, color='blue', alpha=0.2)
plt.fill_between(train_sizes, test_mean - test_std, test_mean + test_std, color='orange', alpha=0.2)

# Labels and Title
plt.title('Learning Curve (F1 Score)', fontsize=16)
plt.xlabel('Training Set Size', fontsize=12)
plt.ylabel('F1 Score', fontsize=12)
plt.legend(loc='best')
plt.grid()
plt.show()

"""## 5.Evaluasi"""

# Prediksi model
y_pred = final_pipeline_svc.predict(X_test)

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
classes = final_pipeline_svc.classes_

# Plot heatmap confusion matrix
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt="d", cmap="YlGnBu", xticklabels=classes, yticklabels=classes)
plt.xlabel("Predicted Labels", fontsize=14)
plt.ylabel("True Labels", fontsize=14)
plt.title("Confusion Matrix", fontsize=16)
plt.tight_layout()
plt.show()

# Cetak classification_report
print("Classification Report model SVM:")
print(classification_report(y_test, y_pred, target_names=classes))

# Store metrics for each model
metrics = {
    "Model": [],
    "Precision": [],
    "Recall": [],
    "F1-Score": []
}

# Definisikan model-model yang sudah dilatih
models = {
    "KNN": final_pipeline_knn,  # Ganti dengan model KNN yang sudah dilatih
    "Logistic Regression": final_pipeline_logistic,  # Ganti dengan model Decision Tree yang sudah dilatih
    "SVM": final_pipeline_svc  # Ganti dengan model SVM yang sudah dilatih
}

# Collect metrics
for name, model in models.items():
    y_pred = model.predict(X_test)  # Prediksi pada data uji
    report = classification_report(y_test, y_pred, output_dict=True)  # Mengambil laporan klasifikasi
    metrics["Model"].append(name)
    metrics["Precision"].append(report['weighted avg']['precision'])  # Precision rata-rata berbobot
    metrics["Recall"].append(report['weighted avg']['recall'])  # Recall rata-rata berbobot
    metrics["F1-Score"].append(report['weighted avg']['f1-score'])  # F1-Score rata-rata berbobot

# Convert to DataFrame for better visualization
df_metrics = pd.DataFrame(metrics)

display(df_metrics.sort_values(by='F1-Score', ascending=False).reset_index().drop(columns='index'))

# Menyimpan model ke file
joblib.dump(final_pipeline_svc, '../model/model_svm_final.pkl')

"""## 6. Kesimpulan

* Model Support Vector Machine (SVM) yang telah dikembangkan menunjukkan hasil yang sangat baik dengan F1-score 99%. Ini menandakan bahwa model ini mampu mengklasifikasikan data dengan sangat baik, terutama dalam menangani ketidakseimbangan antara kelas, yang biasa terjadi pada data pertanian.

Keunggulan Model:

1. F1-Score Tinggi: Dengan F1-score yang mendekati 100%, model ini memiliki kinerja yang sangat baik dalam hal keseimbangan antara precision dan recall, yang sangat penting dalam aplikasi yang melibatkan klasifikasi tumbuhan, di mana kesalahan dalam pemilihan bisa berakibat fatal.
2. Kemampuan Menangani Data Tidak Seimbang: SVM dengan parameter class_weight='balanced' sangat berguna dalam menangani masalah ketidakseimbangan kelas, sehingga membuat model lebih adil dalam memprediksi kelas yang jarang muncul.
3. Akurasi Tinggi: Model ini memberikan akurasi yang tinggi dalam memprediksi tumbuhan yang sesuai dengan kondisi tanah, yang bisa sangat bermanfaat bagi petani dalam memilih tumbuhan yang optimal berdasarkan unsur tanah yang mereka miliki.

Manfaat untuk Petani:

* Model ini berpotensi sangat membantu para petani dalam menentukan jenis tumbuhan yang sesuai dengan kondisi tanah mereka. Misalnya, dengan memasukkan parameter-parameter seperti pH tanah, kelembapan, suhu, dan unsur hara (seperti N, P, dan K), petani dapat dengan cepat mengetahui jenis tumbuhan yang akan tumbuh dengan baik di lingkungan tertentu. Dengan demikian, model ini dapat meningkatkan hasil pertanian, mengurangi pemborosan, dan meningkatkan efisiensi dalam penggunaan sumber daya tanah.

Harapan ke Depan:
 * Dengan hasil yang sangat baik ini, model SVM dapat diintegrasikan dalam aplikasi berbasis web atau mobile yang mudah digunakan oleh petani. Selain itu, dengan penerapan model ini secara lebih luas, diharapkan dapat membantu meningkatkan produktivitas pertanian dan menjaga keberlanjutan pertanian yang ramah lingkungan.

* Secara keseluruhan, model SVM ini dapat menjadi alat yang sangat berguna dalam membantu petani membuat keputusan yang lebih cerdas terkait dengan pemilihan tumbuhan yang sesuai dengan unsur tanah mereka, yang pada gilirannya dapat mendukung peningkatan hasil pertanian yang berkelanjutan.
"""