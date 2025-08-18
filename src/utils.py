import os
import sys
import dill
from src.exception import CustomException
from src.logger import logging


def save_object(file_path: str, obj) -> None:
    """
    Save any Python object as a pickle file using dill.
    Ensures it is always saved inside the 'artifacts' folder at project root.
    """
    try:
        # Always place inside artifacts folder (absolute path)
        artifacts_dir = os.path.join(os.getcwd(), "artifacts")
        os.makedirs(artifacts_dir, exist_ok=True)

        # Force save path inside artifacts
        file_name = os.path.basename(file_path) if file_path else "preprocessor.pkl"
        file_path = os.path.join(artifacts_dir, file_name)

        logging.info(f"Saving object at path: {file_path}")

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

        # Verify creation
        if os.path.exists(file_path):
            logging.info(f"✅ Pickle file successfully saved at {file_path}")
        else:
            logging.warning(f"⚠️ Failed to create pickle file at {file_path}")

    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path: str):
    """
    Load a Python object from a pickle file inside artifacts folder
    """
    try:
        artifacts_dir = os.path.join(os.getcwd(), "artifacts")
        file_path = os.path.join(artifacts_dir, os.path.basename(file_path))

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist")

        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)
