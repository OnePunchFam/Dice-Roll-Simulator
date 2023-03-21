import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window display
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Dice Simulator")

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define the fonts
FONT_LARGE = pygame.font.Font(None, 100)
FONT_SMALL = pygame.font.Font(None, 50)

# Define the dice values
dice_values = [1, 2, 3, 4, 5, 6]

# Download dice images and save as the following
# Define the dice images
dice_images = [
    pygame.image.load("dice-1.png"),
    pygame.image.load("dice-2.png"),
    pygame.image.load("dice-3.png"),
    pygame.image.load("dice-4.png"),
    pygame.image.load("dice-5.png"),
    pygame.image.load("dice-6.png")
]

# Define the roll function
def roll_dice():
    return random.choice(dice_values)

# Define the main function
def main():
    # Set the initial dice value
    dice_value = None
    
    # Create a flag to indicate if the dice has been rolled
    has_rolled = False
    
    # Create a loop to keep the game running
    running = True
    while running:
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dice_value = roll_dice()
                    has_rolled = True
        
        # Fill the window with white
        window.fill(WHITE)
        
        # Draw the title
        title = FONT_LARGE.render("Dice Simulator", True, BLACK)
        window.blit(title, (50, 50))
        
        # Draw the instructions
        instructions = FONT_SMALL.render("Press SPACE to roll the dice", True, BLACK)
        window.blit(instructions, (50, 200))
        
        # Draw the dice image and value
        if has_rolled:
            dice_image = dice_images[dice_value - 1]
            window.blit(dice_image, (200, 250))
            dice_text = FONT_LARGE.render(str(dice_value), True, BLACK)
            window.blit(dice_text, (250, 350))
        
        # Update the display
        pygame.display.update()
    
    # Quit Pygame
    pygame.quit()

# Call the main function
if __name__ == "__main__":
    main()