from PIL import Image
import os

# открываем изображение
def mirror_image(file_path: str,
                 mirror_type: str = "hor"):
    image = Image.open(file_path)

    file_name = file_path.split(os.sep)[-1]
    save_folder = file_path.split(os.sep)[-2]

    # отзеркаливаем по горизонтали
    if mirror_type == "hor":
        mirrored_image = image.transpose(Image.FLIP_LEFT_RIGHT)

    # сохраняем отзеркаленное изображение
    mirrored_image.save(f'{save_folder}/mirrored_{file_name}')
