## 1. Project Setup

### I. Clone the repository to your local machine:
```bash
git clone "https://github.com/siddiqur-54/TaskManager.git"
cd TaskManager
```
### II. Create a virtual environment (optional but recommended):
```bash
python -m venv myvenv
```
Here, myvenv is the name of the virtual environment. You can choose any name according to your project.

### III. Activate the virtual environment:
__For windows:__
```bash
myvenv\Scripts\activate
```
__For Linux/macOS:__
```bash
source myvenv/bin/activate
```
### IV. Install project dependencies:
```bash
pip install -r requirements.txt
```
### V. Database Migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### VI. Create Superuser (Optional):
```bash
python manage.py createsuperuser
```

### VII. Run the Development Server:
```bash
python manage.py runserver
```
Visit http://localhost:8000/ in your web browser

## 2. Setting Up Environmental Variables

To manage sensitive information and configuration settings, this project uses environmental variables. Follow the steps below to set up your `.env` file:

### I. Create a `.env` file:
   Create a file named `.env` in the root of your project.

### II. **Add Configuration:**
   Open the `.env` file and add the following configuration:
   ```env
   DJANGO_SECRET_KEY='your-secret-key'
   DEBUG=1  # Set to 0 for production
   DJANGO_ALLOWED_HOST=your-allowed-host
