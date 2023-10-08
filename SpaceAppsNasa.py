from PIL import Image
import matplotlib.pyplot as plt

def display_image(image_path):
 image = Image.open(image_path)
 plt.imshow(image)
 plt.axis('off')  
 plt.show()


 
image_path = r"D:\Desktop\eclipse.jpeg"
image_path2=r"D:\Documents\eclipse 2.jpeg"
image_path3=r"D:\Documents\hybrid.png"
image_path4=r"D:\Documents\lunat.jpeg"
image_path5=r"D:\Pictures\New folder\table.png" 
image_path6=r"D:\Documents\solar.jpeg"
def display_image(image_path6):
 image = Image.open(image_path6)
 plt.imshow(image)
 plt.axis('off')  
 plt.show()
def display_image(image_path2):
 image = Image.open(image_path2)
 plt.imshow(image)
 plt.axis('off')  
 plt.show()
def display_image(image_path3):
 image = Image.open(image_path3)
 plt.imshow(image)
 plt.axis('off')  
 plt.show()
def display_image(image_path4):
 image = Image.open(image_path4)
 plt.imshow(image)
 plt.axis('off')  
 plt.show()
def display_image(image_path5):
 image = Image.open(image_path5)
 plt.imshow(image)
 plt.axis('off')  
 plt.show()
def story():
    print(''' Once upon a time in a quiet suburban neighborhood, there lived a curious young boy named James. James was a bright 6-year-old who loved spending his days exploring the wonders of the world around him. One sunny afternoon, he was playing in his backyard when something extraordinary happened.

    Suddenly, the sun, which had been shining brilliantly, was covered, and darkness enveloped the entire sky.''')
    display_image(image_path)
    print(''' Startled and scared, James dropped his toys and ran inside his house, his heart pounding with fear. He rushed to find his mother, his tiny voice quivering as he told her about the strange darkness that had fallen from the heavens.

His mother, a kind and knowledgeable woman, couldn't help but chuckle at her son's wide-eyed astonishment. She knelt down to his level and gently reassured him. "James, don't be afraid," she said, her warm smile comforting him. "What you witnessed was not a scary event, but something quite fascinating. It was an eclipse."

Eager to learn more, James listened intently as his mother explained. "You see," she continued, "an eclipse occurs when one celestial body, like the Moon or Earth, passes into the shadow of another celestial body."

With growing curiosity, James asked, "Are there different kinds of eclipses?"

His mother nodded, "Indeed, there are two main types: solar eclipses, which happen when the Moon comes between the Earth and the Sun, blocking out the Sun's light, and lunar eclipses, where the Earth passes between the Sun and the Moon, casting its shadow on the Moon."

James was captivated by this newfound knowledge and had more questions pouring from his inquisitive mind.

His mom patiently answered, "Eclipses are special because only a few people on Earth can see them at any given time. It all depends on the alignment of the Sun, Moon, and Earth. If they're perfectly aligned, people in certain regions get to witness the eclipse."

"Why don't we see them all the time?" James asked.

His mother explained, "Eclipses are not constant because the alignment needs to be just right. It's like a celestial dance, and sometimes they align, and sometimes they don't."

James was curious about what caused this celestial dance. "How do the Moon, Earth, and Sun align like that?"

With a smile, his mother replied, "It's all about their orbits, James. When these celestial bodies align in a straight line, one of them casts a shadow on the other, creating an eclipse."

The young boy's eyes widened as he absorbed this newfound knowledge. "Do eclipses happen often?"

His mother answered, "Eclipses do occur relatively frequently, but their frequency varies. On average, there are about two to five solar eclipses and two to four lunar eclipses each year. However, not all of them are visible from the same location on Earth."

Fascinated by the idea of predicting celestial events, James asked, "How do scientists know when and where eclipses will happen?"

His mother explained, "Scientists use precise calculations based on the known orbits of the Moon and Earth to predict eclipses. These calculations allow astronomers to forecast when and where eclipses will occur many years in advance."

As their conversation continued, James learned more about the differences between lunar and solar eclipses and discovered the concept of eclipse seasons. His mother patiently answered each question, nurturing his curiosity about the marvels of the universe.

In the end, James had not only witnessed a rare celestial event but had also embarked on a journey of discovery that would fuel his passion for science and the mysteries of the cosmos for years to come. And as he looked up at the starry night sky that evening, he couldn't help but feel a sense of wonder and gratitude for the knowledge his mother had shared.

The story of James and his newfound fascination with eclipses was just the beginning of his exciting journey into the world of science, where the universe's mysteries awaited him at every turn.
''')

def Q1():
    print(" A solar eclipse happens" 
        "when the Moon passes directly between the Sun and Earth. When the "
        "Moon completely blocks the Sun, it is called a total solar eclipse."
        "When the Moon only blocks part of the Sun, it is called a partial eclipse."
        "An annular eclipse is s special type of partial eclipse that happens when" 
        "the Moon blocks all of the Sun except for a small ring around the edge. "
        "Sometimes a solar eclipse can appear as an annular in some places and a "
        "total in others as the Moon's shadow moves across Earth's surface. This is known as a hybrid eclipse."
        )
    display_image(image_path2)
  

def Q2():
    print('''
        "Eclipses are visible only from specific regions of the Earth where the alignment between the Sun, Moon, and Earth allows for it.
        Those who are in the path of the eclipse will see it, while others outside of this path won't witness it."
        ''')

def Q3():
    print('''
        The alignment of the Sun, Moon, and Earth during an eclipse is due to the orbits
        of these celestial bodies. It happens when the three objects align in a straight
        line, with one of them casting a shadow on the other. 
         ''')
    display_image(image_path4)
    display_image(image_path6)
    display_image(image_path3)

def Q4():
    print('''
         "Eclipses occur relatively frequently, but their frequency varies. On average, there are about two to five solar eclipses and two 
         to four lunar eclipses each year. However, not all of them are visible from the same location on Earth."
        ''')

def Q5():
    print(''' 
         Scientists can predict eclipses using preciselculations based on the known orbits of the Moon and Earth. These calculations allow astronomers to 
         forecast when and where eclipses will occur many years in advance.
        ''')
    display_image(image_path5)
def Q6():
    print('''
        A lunar eclipse occurs when the Earth comes between the Sun and the Moon, causing the Earth's shadow to be cast on the Moon. This results in the Moon appearing to darken or turn a reddish hue.
        On the other hand, a solar eclipse happens when the Moon passes between the Earth and the Sun, blocking out the Sun's light and casting a shadow on the Earth. During a solar eclipse, the Sun appears to be covered by the Moon, causing a temporary darkness during the day.
        ''')

def Q7():
    print('''
        Eclipse seasons occur because the Moon's orbit is tilted relative to the Earth's orbit around the Sun. This tilt means that the Moon, Earth, and Sun do not always align perfectly, but they come close to alignment during specific times of the year. These times are known as eclipse seasons, and they occur roughly every six months.
        During an eclipse season, either a solar or lunar eclipse is more likely to happen because the Sun, Moon, and Earth are closer to being in line with each other.
        ''')
    import cv2
    cap = cv2.VideoCapture(r"D:\Desktop\Untitled video - Made with Clipchamp (13).mp4") 
    if not cap.isOpened():
        print("Error: Could not open video file.")
        exit()
    while True:
        ret, frame = cap.read()
        if not ret:
            break  
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break 
    cap.release()
    cv2.destroyAllWindows()

def IntroScene():
    print('''
          Hello! Today I am going to explain to you what are eclipses and what are their types. Input the question numbers for answers. Also, start from the beginning for a fun story.

1.How do eclipses occur?
2.Why do only some people on Earth see an eclipse at a given time?
3.What causes the Sun, Moon, and Earth to align?
4.How often do eclipses occur?
5.How do scientists know when and where eclipses will occur?
6.What is the difference between a lunar and solar eclipse?
7.What is an eclipse season and why do they occur approximately every six months (or twice a year)?
For complete story enter "story"''')
def main():
    IntroScene()
    while True:
        question_num = input('Enter the question number (1-7) or "exit" to quit: ')
        if question_num == "exit":
            break
        elif question_num == "1":
            Q1()
        elif question_num == "2":
            Q2()
        elif question_num == "3":
            Q3()
        elif question_num == "4":
            Q4()
        elif question_num == "5":
            Q5()
        elif question_num == "6":
            Q6()
        elif question_num == "7":
            Q7()
        elif question_num=="story":
            story()
        else:
            print("Invalid question number. Please enter a valid question number (1-7) or 'exit' to quit.")

if __name__ == "__main__":
    main()