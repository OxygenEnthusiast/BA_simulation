from anim.ani import Animation
import argparse

def main(theorem):
    animation = Animation(theorem)
    while animation.running:
        animation.draw()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="simulates random walkers")
    parser.add_argument('theorem', type=str,choices=['no','il','clt','slln'], help='shortcut for theorem')
    args = parser.parse_args()
    main(args.theorem)


