import random
from os.path import exists

class Image:
    def __init__(self, name, url):
        self.name = name
        self.url = url

class ImageList:
    def __init__(self, file_path='aux_info/images.txt'):
        self.images = []
        self.file_path = file_path
        if exists(file_path):
            self.load()

    def add_image(self, img):
        if img.name not in [i.name for i in self.images]:
            self.images.append(img)
            self.save()
            return True
        return False
    
    def remove_image(self, name):
        for i in self.images:
            if i.name == name:
                self.images.remove(i)
                self.save()
                return True
        return False
    
    def print_images(self):
        for i in self.images:
            print(f'{i.name}: {i.url}')

    def save(self):
        with open(self.file_path, 'w') as f:
            for image in self.images:
                f.write(f'{image.name} {image.url}\n')

    def load(self):
        with open(self.file_path, 'r') as f:
            for line in f.readlines():
                name, url = line.split()
                self.add_image(Image(name, url))

    def get_image(self, name):
        for i in self.images:
            if i.name == name:
                return i
        return None

    def get_random_image_path(self):
        return random.choice(self.images).url
    
images = ImageList()

images.add_image(Image("cage1", "https://img.olhardigital.com.br/wp-content/uploads/2023/05/super-homem-nicolas-cage.png"))
images.add_image(Image("cage2", "https://i.guim.co.uk/img/media/dd3882c4ad0fd11a14cffc7e5edaabe5ce8a8b53/0_85_1077_646/master/1077.jpg?width=700&quality=85&auto=format&fit=max&s=c906598d7b435814a7e49a5ee4779c2f"))
images.add_image(Image("cage3", "https://www.liveabout.com/thmb/t0DACGkX-c_frflRNQ_OG37YZ5E=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/nicolas-cage-mona-lisa-5798ce3d5f9b589aa975f7b7.jpg"))
images.add_image(Image("cage4", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSk8Z8wpuyrjDydhoNOOwzZaOlODgfEFyT37w&usqp=CAU"))
images.add_image(Image("cage5", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsH4RwzIWgvpD3au3IEurRIcb4HTlZO_ilIw&usqp=CAU"))
images.add_image(Image("cage6", "https://i.seadn.io/gae/Q2VmCetcE082J0PhisdQidWqr8Smkj5-dWPtcr4-C8OWxqLLt1PiPwn2eQ2FpEkf7_7LkAqFDnjyYOT2Vkasn6pD5-We0v2Fh4ms?auto=format&dpr=1&w=1000"))
images.add_image(Image("cage7", "https://i.pinimg.com/564x/29/b5/8c/29b58c47c5126cc4766f81b5ddb3e285.jpg"))
images.add_image(Image("cage8", "https://ih0.redbubble.net/image.1603557678.9463/raf,360x360,075,t,fafafa:ca443f4786.jpg"))
images.add_image(Image("cage9", "https://www.hollywoodreporter.com/wp-content/uploads/2023/11/Nicolas-Cage-Dream-Scenario-Premiere-GettyImages-1670833155-H-2023.jpg?w=1296"))

images.print_images()