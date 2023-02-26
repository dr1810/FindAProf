from PIL import Image
def home_tab(tab1):
    tab1.title("Our Vision and Our Why")
    tab1.write(
        "The core idea of our web application is to find the right professor in your university for your required course.")
    tab1.write(
        "In today\'s world, there are so many people and websites from whom you get recommendations and to choose the best suited professor to teach you is a very difficult choice to make.")
    tab1.write("But in the end, not everyone ends up being happy with their choice because of reasons such as:")
    tab1.write("1. You find it hard to do the assignments the professor gives you.")
    tab1.write("2. You find it hard to understand what the professor teaches you.")
    tab1.write("3. The class environment was too competitive or not conducive for you to learn well.")
    tab1.write("and the list goes on.")
    tab1.write(
        "This can be prevented by making the right choice based on your abilities and will help you find the right mentor who can guide you.")
    tab1.write(
        "This application is inspired by the movie **Moneyball** where Billy Beane(Brad Pitt) uses the minimal funds given by Oakland Athletic to come up with a match winning team.")
    tab1.write(
        "In the movie, Billy Beane works with an economist from Yale where they scout for the best players using the given budget.")
    tab1.write(
        "Both of them use machine learning based algorithms to find the best players statistically and not with mere instinct, which in the end led the Oakland Athletic team to win 20 games straight from their losing form of losing 7 games in a row.")
    tab1.write(
        "Inspired by the film, we have come up with this idea to help you to have the best learning experience from the best available faculty in your college.")
    img = Image.open("C:\\Users\\dharu\\PycharmProjects\\Ureackathon\\home_page.jpeg")
    tab1.image(img)