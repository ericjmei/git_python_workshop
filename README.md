# git_python_workshop
August 2025 workshop on git, python, and linting for the Turner Group

# getting started
The first step is cloning this repository. On the command line, change (`cd`) to the directory you want to clone the repository into. Then,
```bash
git clone https://github.com/ericjmei/git_python_workshop.git
```

Now, we need to create an environment. We have a few options for doing this: virtual environments, conda environments, or pixi environments. Choose your fighter.

## virtual environment
```bash
python -m venv venv
source venv/bin/activate # might be different on windows
pip install -r requirements.txt
```

## conda environment
```bash
conda create --name git_python_workshop
conda activate git_python_workshop
pip install -r requirements.txt
```

## pixi environment
```bash
pixi install
```