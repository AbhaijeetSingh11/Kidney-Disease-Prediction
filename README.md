
````markdown
# Kidney Disease Classification with MLflow & DVC

An end-to-end Deep Learning project to classify Kidney Diseases from CT scan images using a Convolutional Neural Network (CNN). This project integrates **MLflow** for experiment tracking & model registry, and **DVC (Data Version Control)** for dataset versioning and ML pipeline orchestration.

---

## 🚀 Project Workflow

1. **Update Configuration Files**
   - `config.yaml` - General configurations (paths, model details, etc.)
   - `params.yaml` - Hyperparameters (learning rate, batch size, etc.)
   - `secrets.yaml` (Optional) - API keys, credentials (if needed)
   - Update **entity classes** and **configuration manager** in `src/config/`

2. **Update Components**
   - Data Ingestion
   - Model Training
   - Evaluation
   - Model Pusher

3. **Update Pipeline Scripts**
   - Orchestrate pipeline stages in `src/pipeline/`

4. **Update Main Scripts**
   - `main.py` for running the pipeline
   - `dvc.yaml` for defining DVC stages

5. **Run Streamlit or Flask App**
   - `app.py` to visualize predictions (local web app)

---

## 🛠️ How to Run this Project?

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/krishnaik06/Kidney-Disease-Classification-Deep-Learning-Project
cd Kidney-Disease-Classification-Deep-Learning-Project
````

### 2️⃣ Create a Conda Environment

```bash
conda create -n cnncls python=3.8 -y
conda activate cnncls
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App Locally

```bash
python app.py
```

### 5️⃣ Open in Browser

Visit: `http://localhost:5000/` (or the port specified)

---

## 🔍 MLflow Experiment Tracking

### Start MLflow UI Locally

```bash
mlflow ui
```

### Or Use Dagshub MLflow Tracking Server

```bash
# Set MLflow Tracking Environment Variables
export MLFLOW_TRACKING_URI=url_from_repo_in_dagshub
export MLFLOW_TRACKING_USERNAME=username_of_dagshub
export MLFLOW_TRACKING_PASSWORD=dagshub_password

# Run your MLflow scripts
python script.py
```

---

## 📦 DVC - Data & Pipeline Versioning

### Initialize DVC in Project

```bash
dvc init
```

### Run Entire ML Pipeline (Reproduce Stages)

```bash
dvc repro
```

### Visualize Pipeline DAG

```bash
dvc dag
```

---

## 🧰 Tools & Technologies

* Python 3.8
* TensorFlow / Keras (CNN Model)
* MLflow (Experiment Tracking & Model Registry)
* DVC (Data Version Control & Pipeline Orchestration)
* Flask (Deployment API)
* Docker (Containerization) \[Optional]
* Dagshub (Remote MLflow & DVC storage)

---

## 📚 About MLflow & DVC

### MLflow

* Production-grade experiment tracking
* Tracks parameters, metrics, and artifacts
* Model versioning & registry
* UI for visualizing experiment runs

### DVC

* Lightweight data & model versioning tool
* Reproducible pipelines (orchestration)
* Ideal for POCs and collaborative data science projects
* Remote storage support (S3, GDrive, Azure, etc.)

---

## 💡 Credits

Project inspired by [Krish Naik's Deep Learning Project Series](https://github.com/krishnaik06)

---
