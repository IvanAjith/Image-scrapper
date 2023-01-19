from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import io
import os
from PIL import Image
import time

PATH = "Users/ajithsmacbookair/Downloads/chromedriver_mac_arm64 2/chromedriver"
q = query = "ajith"
directory = q
parent_dir = "/Users/ajithsmacbookair/Downloads/ImageScrapper/images"
mode = 0o666
path2 = os.path.join(parent_dir, directory)
os.mkdir(path2)


wd = webdriver.Chrome(PATH)

def get_images_from_google(q, wd, delay, max_images):
	def scroll_down(wd):
		wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(delay)

	url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"
	wd.get(url.format(q=query))

	image_urls = set()
	skips = 0

	while len(image_urls) + skips < max_images:
		scroll_down(wd)

		thumbnails = wd.find_elements(By.CLASS_NAME, "Q4LuWd")

		for img in thumbnails[len(image_urls) + skips:max_images]:
			try:
				img.click()
				time.sleep(delay)
			except:
				continue

			images = wd.find_elements(By.CLASS_NAME, "n3VNCb")
			for image in images:
				if image.get_attribute('src') in image_urls:
					max_images += 1
					skips += 1
					break

				if image.get_attribute('src') and 'http' in image.get_attribute('src'):
					image_urls.add(image.get_attribute('src'))
					print(f"Found {len(image_urls)}")

	return image_urls


def download_image(download_path, url, file_name):

	try:
		image_content = requests.get(url).content
		image_file = io.BytesIO(image_content)
		image = Image.open(image_file)
		file_path = download_path + file_name

		with open(file_path, "wb") as f:
			image.save(f, "JPEG")

		print("Success")
	except Exception as e:
		print('FAILED -', e)

urls = get_images_from_google(q,wd, 2, 5)

for i, url in enumerate(urls):
	download_image('images/'+q+'/', url, str(i) + ".jpg")



wd.quit()