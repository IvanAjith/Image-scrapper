# Image-scrapper using Chrome browser. 
NOTE :This code will works only if you have a chrome browser 

This code will help the user to search and download the n number of google images of a inoput query and store in locally. 
To make this code works, I have imported the basic libraries such as selenum, requests, Imgae and time 

I also download the chrome driver and declared the path of the executable file as PATH (LINE 9)
I claaed a variable called "q" which is the user input to get the required file to be search and download 
Created a path (directory) with the q as the main folder so that the results will be downloaded under this folder everytime the code execute for a particular q value 

get_image_from_google is a function that takes 4 variables namely 
  (i)   q (the search quiery),
  (ii)  wd (the chrome webdriver)
  (iii) delay (the time delay for each action)
  (iv)  max_images (the number of images you wan to search and store locally)
  
 scroll_down is the function under the get_images_from_google function which takes the webdriver as input and scroll the search result in the chrome to the very last to load all the images 
  
 Declared a variable called image_urls as set to store all the source urls of the searched images for further scrapping. 
  
 Used the while loop to identify the thumbnail classes and click each images as long as the   length of image_urls < max_images
 
 Once the main image is opened, used a for loop to extract the source link of that corresponding class of all images and store it in the image_urls
 
 download_images function will use the following 3 inputs :
  (i) download_path 
  (ii) url
  (iii) file_name 
  
Extracted the content of the saved urls (the actual picture) using the .content function and declared the filepath of that image. 
 
The final 2 steps to execute the code 
    (i) use the get_image_from_google function and store all the urls in image_urls set and save it as "urls"
    (ii) call this 'urls' inside the  download_image function and use a for loop to enumerate and store the images in the declared path or directory
    
 wd.quit() will close this code once everything executed successfully. 
 
  
