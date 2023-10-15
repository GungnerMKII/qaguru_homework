import pytest
import os
import shutil
from utils import TMP_PATH

@pytest.fixture(scope='session', autouse=True)
def create_delete_tmp():
    if not os.path.exists(TMP_PATH):
        os.mkdir('tmp')
        
    yield
    shutil.rmtree(TMP_PATH)