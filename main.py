import streamlit as st
import cv2

def new_line(n = 1):
    for _ in range(n):
        st.markdown("<br>", unsafe_allow_html=True)


st.markdown("<h1 align='center'> Basel ❤️ Jumana </h1>", unsafe_allow_html=True)
st.markdown("<h5 align='center'> 2023-08-07 </h1>", unsafe_allow_html=True)

new_line()

st.write("""

I love you so much Jumana, and I can't wait to spend the rest of my life with you. I'm so excited to see what the future holds for us. I love you so much BABY ❤️❤️❤️❤️❤️❤️❤️❤️❤️

You are the best thing that has ever happened to me. You are my **everything**. 
You are my **Love**, my **Life**, my **Happiness**, my **Juju**, my **Sunshine**, my **Heart**, my **Soul**, my **Dreams**, my **Fantasies**, my **Reality**, my **Future**, my **Past**, my **Present**, my **Forever**, my **Always**, my **Forever and Always**, my **Everything**.         
         """)

st.markdown("<h1 align='center'> 🎉🎉🎉🎉🎉🎉🎉🎉🎉 </h1>", unsafe_allow_html=True)

st.divider()

st.header("Some Memories ❤️")

new_line(1)

st.subheader("How Much I Love You ❤️")
with st.expander("Click to see"):
    col1, col2 = st.columns([1, 0.65], gap='large')

    col1.markdown("""
                  
                  <br>

                I love you to the moon and back, to infinity and beyond, forever and ever. I love you unconditionally.
                I love you more than anything in this world. I love you more than life itself. I love you more than anything in this world could ever compare to.
                
                I love you more than words can describe. I love you more than I love myself. I love you more than my life, because you are my life.
                I care about you more than I care about myself. I fraid about you more than I fraid about myself. I draw my future and my life with you.
                I can't imagine my life without you. I can't imagine my future without you.
                  
                I love everything about you. I love your eyes, your smile, your lips, your hair, your body, your voice, your laugh, your smell, your touch, your hugs, your hands, your legs, (your you know what 😉), your literally everything.
                    """, unsafe_allow_html=True)

    col2.image("assets/img1.jpg",)

    st.divider()
    new_line(1)

    col1, col2, col3 = st.columns(3)

    img2 = cv2.imread("assets/img2.jpg")

    col1.image("assets/img2.jpg", width = 200, caption = "Your Hands")
    col2.image("assets/img3.jpg", width = 200, caption = "Your Lips")
    col3.image("assets/img4.jpg", width = 200, caption = "Your Eyes")

    col1, col2, col3 = st.columns(3)
    col1.image("assets/img5.jpg", width = 200, caption = "Your Smile")
    col2.image("assets/img6.jpg", width = 200, caption = "Your Laugh")
    col3.video("assets/vid1.mp4",)

new_line(2)
st.subheader("Why I Love You ❤️")
with st.expander("Click to see"):

    new_line(1)
    col1, col2 = st.columns([1, 0.37])
    col1.image("assets/img8.jpg")
    col2.image("assets/img7.jpg")

    new_line(1)
    st.markdown("""
    
    I love you because you were there for me when no one else was. I love you because you are the only one who showed me the true meaning of love, life, happinies, and everything beatiful.
    
    I love you beause you kept patient with me when I was at my worst. I love you because you are the only one who can make me feel better when I'm sad.
    I love you because you are beautiful, smart, has pure heart, and you are the most amazing person I've ever met.

    I love you because I believe that together, we can do anything literally anything. We can build massive things, we can change the world, we can do anything we want.
    I love you because I believe that together, we can make our dreams come true.

                       
                """)

    new_line(1)
    col1, col2, col3 = st.columns(3)

    col1.image("assets/img9.jpg", width = 200, )
    col2.image("assets/img11.jpg", width = 200,)
    col3.image("assets/img10.jpg", width = 200, )


new_line(2)
st.subheader("How Much I Need You ❤️")
with st.expander("Click to see"):

    new_line(1)
    st.markdown("""

    I need you more than anything in this world. I need you to stay beside me forever. I need you to be my wife, my partner, my best friend, my love, my everything.
    
    You did so much for me, and you will do more, and I will do more for you too. I will do everything I can to make you happy, to make you feel loved, safe, comfortable, secure, and to make you feel like you are the most important person in this world **BECAUSE YOU ARE**.
                
    I promise that I will support you no matter what, and I will be there for everytime you need me. I will be there in your sadnes, in your happiness, in your success, in your failure, in your good times, and in your bad times.

                
    I promise that I will be there beside you in every step you take, and I will be there to help you, to support you, to guide you, to protect you, to love you, to care about you
    """, unsafe_allow_html=True)

    new_line(1)

    col1, col2, col3 = st.columns(3)
    col1.image("assets/img12.jpg", width = 200, )
    col2.video("assets/vid2.mp4",)
    col3.image("assets/img13.jpg", width = 200,)


new_line(2)
st.subheader("Our Story ❤️")
with st.expander("Click to see"):

    new_line(1)
    st.write("I still remember the first photo for us with (this stupid Yahia boy **ya3 nnnn**). It was at the end of 2021 I guess. When I made this photo and I want you to know a little bit with just a hint that I love and I need you in my life. Still sure that My Design is better than yours 🧿")

    col1, col2 = st.columns(2)
    col1.image("assets/img14.jpg",  caption = "My Design")
    col2.image("assets/img15.jpg",  caption = "Your Design")

    col1, col2 = st.columns([1, 0.4])
    col1.write(" \n\n\nThen we have our first video at the University, Oh my god, I love this video so much wallah, you are so cute and amazing.")
    col1.markdown("<br>", unsafe_allow_html=True)
    
    col1.write("Look at your eyes, your smile, and look at me how much I am fell in love with you. I love you so much Habebti Wallah ❤️")
    col1.markdown("<br>", unsafe_allow_html=True)

    col1.write("After that, we went to give me my birthday gift, god I love that gift it means a lot to me wallah. ")
    col1.markdown("<br>", unsafe_allow_html=True)

    col1.write("We took this photo together, and in that day, I felt something different, I was shocked with the way you are treating me, with you way of love. I felt that I can't live without you and I can't let you go.")
    col2.video("assets/vid3.mp4",)

    st.image("assets/img16.jpg",  caption = "My Birthday Gift")


    st.write("Then, We started to love each other silently and do our besties routine. We stay together, we have the same duck at our bags, keep your legs on mine, and recording videos for me for your Eid Outfit. I love you, I love your outfits, I love our routine, I love everything with you my love ❤️")
    col1, col2, col3, = st.columns(3)

    col1.video("assets/vid4.mp4",)
    col2.video("assets/vid5.mp4",)
    col3.video("assets/vid6.mp4",)

    col1, col2, col3, = st.columns(3)
    col1.image("assets/img18.jpg", )
    col2.image("assets/img19.jpg", )
    col3.image("assets/img20.jpg", )

    new_line(1)
    st.write("After that, we started to love each other more and more, and we say it to each other. We started to go out together, have fun together, spending time together, and we shared that love with our friends.")
    st.write("We started to be lovers, we started to be partenrs, we started to be the most important person for each other.")
    st.write("We started to go out, sitting in the car having some fun, holding hands, listend to music (Nefsi Ahabik). I love you so so so so so much wallah ya Habebti ❤️")
    st.write("**We started to be a FOREVER KIND OF THING** ❤️"  )

    col1, col2, col3, = st.columns(3)
    col1.image("assets/img21.jpg", )
    col2.image("assets/img22.jpg", )
    col3.video("assets/vid7.mp4",)

    col1, col2, col3, = st.columns(3)
    col1.image("assets/img26.jpg", )
    col2.image("assets/img24.jpg", )
    col3.image("assets/img25.jpg", )

    col1, col2, col3, = st.columns(3)
    col1.image("assets/img23.jpg", )
    col2.image("assets/img28.jpg", )
    col3.image("assets/img27.jpg", )

    new_line(1)
    st.write("I want to keep writing, but I will not finish, it is a beginning journey with no ends. All I want to say is that:")
    st.write("I love you so much Habebti, you are my love, my life, my heart, my soul, my secure angel, my daughter, my wife, my everything. I love you so much wallah ❤️")
    st.write("I will do whatever it takes to make you happy, to have you, and to be together under the same roof, and to be together forever and always ❤️. To have a beautiful life, beautiful family, beautiful wife, and beautiful future ❤️")

    new_line(1)
    col1, col2 = st.columns(2)
    col1.markdown("<h4 align='center'> Happy Birthday </h4>", unsafe_allow_html=True)
    col1.video("assets/vid9.mp4",)
    col2.markdown("<h4 align='center'> My Beautiful Wife ❤️ </h4>", unsafe_allow_html=True)
    col2.video("assets/vid8.mp4",)

    st.markdown("<h4 align='center'> I love you So Much ❤️ </h4>", unsafe_allow_html=True)
    st.image("assets/img29.jpg")
