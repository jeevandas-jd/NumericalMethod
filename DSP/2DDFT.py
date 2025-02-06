import numpy as np

import matplotlib.pyplot as plt

from PIL import Image

def discreateFouriorTransorm(image):
    N, M = image.shape 
    result = np.zeros((N, M), dtype=complex)

    for k in range(N):
        for l in range(M):

            sum=0
            for i in range(N):
                for j in range(M):

                    exponent=2*j+np.pi*((k * i / N) + (l * j / M))

                    sum+=image[i,j]*np.exp(exponent)
            result[k,l]=sum
    
    return result

if __name__=="__main__":

    Image_path="image2.webp"

    img = Image.open(Image_path).convert("L") 

    img_array=np.asarray(img)

    print(img_array)

    result=discreateFouriorTransorm(img_array)

    print(f"array after 2D Discrete Fouriour Transform \n{result}")

