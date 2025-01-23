# Dizin Listeleme Aracı

Bu Python betiği, belirtilen bir dizindeki tüm alt dizinleri ve dosyaları listeler ve bunları bir metin dosyasına yazar. Ayrıca, belirli dosya ve klasörleri yok sayma özelliği de sunar.

## Kullanım

1.  Bu depoyu bilgisayarınıza klonlayın veya `dizin_listeleme.py` dosyasını indirin.
2.  Python 3'ün kurulu olduğundan emin olun.
3.  Komut satırında veya terminalde betiğin bulunduğu dizine gidin.
4.  Betiği çalıştırmak için aşağıdaki komutu kullanın:

    ```bash
    python dizin_listeleme.py
    ```

5.  Sizden listelenecek dizin yolunu ve yok sayılacak dosya/klasörleri girmeniz istenecektir. Yok sayılacak birden fazla öğe varsa, bunları virgülle ayırarak girin. Örneğin: `dosya1.txt,klasor2,gizli_dosya.txt`
6.  Listelenen dizin ve dosyalar `dosya_listesi.txt` adlı bir dosyaya kaydedilecektir.

## Özellikler

*   Belirtilen dizindeki tüm alt dizinleri ve dosyaları listeler.
*   Yok sayma listesi ile belirli dosya ve klasörleri listelemeden hariç tutma.
*   UTF-8 kodlaması ile dosya oluşturma.
*   Kullanıcıdan dizin yolunu ve yok sayılacak öğeleri alma.
*   Hata yönetimi ile dosya bulunamadığında veya başka bir hata oluştuğunda bilgilendirme.

---

# Directory Listing Tool

This Python script lists all subdirectories and files within a specified directory and writes them to a text file. It also offers the ability to ignore specific files and folders.

## Usage

1.  Clone this repository to your computer or download the `dizin_listeleme.py` file.
2.  Make sure you have Python 3 installed.
3.  Open a command prompt or terminal and navigate to the directory where the script is located.
4.  Use the following command to run the script:

    ```bash
    python dizin_listeleme.py
    ```

5.  You will be prompted to enter the directory path to be listed and the files/folders to be ignored. If there are multiple items to ignore, separate them with commas. For example: `file1.txt,folder2,hidden_file.txt`
6.  The listed directories and files will be saved to a file named `dosya_listesi.txt`.

## Features

*   Lists all subdirectories and files within the specified directory.
*   Excludes specific files and folders from the listing using an ignore list.
*   Creates the file with UTF-8 encoding.
*   Gets the directory path and items to ignore from the user.
*   Error handling to inform the user if the file is not found or another error occurs.
