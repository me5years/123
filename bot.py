import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def run_troll():
    print("Настройка браузера...")
    options = Options()
    options.add_argument("--headless") # Запуск без экрана
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # Эмуляция вебкамеры
    options.add_argument("--use-fake-ui-for-media-stream")
    options.add_argument("--use-fake-device-for-media-stream")
    
    # Указываем путь к видеофайлу, который мы создадим в GitHub Actions
    video_path = os.path.abspath("video.y4m")
    options.add_argument(f"--use-file-for-fake-video-capture={video_path}")

    # Запуск Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        print("Заходим на сайт одноклассника...")
        driver.get("https://mcjemods.wuaze.com/sdam-vpr/vpr_fisika/")
        
        # Ждем 45 секунд (чтобы видео успело проиграться и отправиться)
        print("Ждем отправки видео (45 сек)...")
        time.sleep(45) 
        print("Готово! Одноклассник получил подарок.")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    run_troll()
