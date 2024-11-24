import threading
import requests
import os

# ჩამოსატვირთი ფაილების ლინკები
mp3_urls = [
    "https://www.example.com/song1.mp3",
    "https://www.example.com/song2.mp3",
    "https://www.example.com/song3.mp3",
]

# ფაილის ჩამოტვირთვის ფუნქცია
def download_mp3(url, filename):
    # მივიღოთ ამჟამინდელი დირექტორია
    current_directory = os.getcwd()
    # შევქმნათ სრული გზა ფაილის შესანახად
    full_filename = os.path.join(current_directory, filename)

    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(full_filename, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"{filename} ჩამოტვირთვა დასრულდა.")
        else:
            print(f"{filename} ჩამოტვირთვა ვერ მოხერხდა. სტატუსი: {response.status_code}")
    except Exception as e:
        print(f"შეცდომა {filename}-ის ჩამოტვირთვისას: {e}")

# ძაფების შექმნა და გაშვება
threads = []
for i, url in enumerate(mp3_urls):
    filename = f"song{i+1}.mp3"
    thread = threading.Thread(target=download_mp3, args=(url, filename))
    threads.append(thread)
    thread.start()

# ველოდებით ყველა ძაფის დასრულებას
for thread in threads:
    thread.join()

print("mp3 ფაილების ჩამოტვირთვის პროგრამა დასრულდა.")