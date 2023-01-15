import shutil

dir_to_zip = '/Users/macbook/Documents/Programação/Curso PY/Módulos Avançados/Zipping/extracted_cont'

nome_do_output = "shutil_extracted_zip"

shutil.make_archive(nome_do_output, 'zip', dir_to_zip)

# shutil.unpack_archive('shutil_extracted_zip', 'final_unzip', 'zip')