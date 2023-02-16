from photo_organiser.services.file_service import FileService
import pytest
import os

@pytest.mark.parametrize('name', ['data\\images'])
def test_get_list_filenames(name) -> None:

    service = FileService()
    folder = os.path.join(os.path.dirname(__file__), name)
    result = service.get_list_filenames(folder)

    print(result)

    assert result is not None
    assert type(result) == list
    assert len(result) == 3
    