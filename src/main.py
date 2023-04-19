from anim.ani import Animation

def main():
    animation = Animation()
    print(animation.walkers)
    while animation.running:
        animation.draw()


if __name__ == "__main__":
    main()


