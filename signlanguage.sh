#!/bin/bash

# Define the virtual environment directory
venv_dir=".venv"

# Check if the virtual environment directory exists, and if not, create it
if [ ! -d "$venv_dir" ]; then
    echo "Creating virtual environment..."
    python3 -m venv "$venv_dir"
fi

# Activate the virtual environment
source "$venv_dir/bin/activate"

# Function to check if a file exists
check_file_exists() {
    if [ -f "$1" ]; then
        return 0  # File exists
    else
        return 1  # File does not exist
    fi
}

# Check if the model file exists
model_file="Resources/SLmodel.keras"
if check_file_exists "$model_file"; then
    echo "Model file exists."
else
    # Check if build_model.py and data files exist
    build_script="build_model.py"
    train_csv="Resources/train.csv"
    test_csv="Resources/test.csv"

    if check_file_exists "$build_script" && check_file_exists "$train_csv" && check_file_exists "$test_csv"; then
        read -p "Model file does not exist. Do you want to build the model? (y/n): " user_input
        if [ "$user_input" == "y" ]; then
            echo "Building the model..."
            python build_model.py
            echo "Model has been built."
        else
            echo "Model not built."
        fi
    else
        echo "Required files not found. Please ensure that build_model.py, train.csv, and test.csv exist in the Resources folder."
    fi
fi

# Check for dependencies and install them using pip if missing
required_dependencies=("numpy" "pandas" "tensorflow" "scikit-learn" "opencv-python")
for dependency in "${required_dependencies[@]}"; do
    if ! python -c "import $dependency" &> /dev/null; then
        echo "Installing $dependency..."
        pip install "$dependency"
    fi
done

# Ask if the user wants to run the sign language model
read -p "Do you want to run the sign language model? (y/n): " run_model_input
if [ "$run_model_input" == "y" ]; then
    python test_model.py
    echo "Sign language model has been run."
else
    echo "Exiting without running the sign language model."
fi

# Deactivate the virtual environment
deactivate
