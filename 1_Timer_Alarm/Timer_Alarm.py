from rich.console import Console
import pygame
import time

# Create a Console instance
console = Console()

def main():
    # Initialize pygame
    pygame.init()
    try:
        # Clear the console
        clear_console()
        hours = int(input("How many HOURS to wait? : "))
        minutes = int(input("How many MINUTES to wait? : "))
        seconds = int(input("How many SECONDS to wait? : "))
        total_time = (hours * 3600) + (minutes * 60) + seconds
        if not 0<=minutes<60 and not 0<=seconds<60:
            raise ValueError
        # Begin the Timer
        start(total_time)
        clear_console()
        console.print("[bold red]TIME UP!!![/bold red]")
        play_alarm("alarm_ringtone.mp3")
    except ValueError:
        console.print("[bold red]Invalid input. Please enter VALID numeric values.[/bold red]")
    except Exception as e:
        console.print(f"[bold red]An error occurred: {e}[/bold red]")
    finally:
        pygame.quit()

# Function to begin the Timer
def start(total_time):
    time_elapsed = 0

    while time_elapsed <= total_time:
        time.sleep(1)
        time_left = total_time - time_elapsed
        hours_left = time_left // 3600
        minutes_left = (time_left % 3600) // 60
        seconds_left = time_left % 60
        clear_console()
        console.print(f"Time Left: [bold green]{hours_left:02d}[/bold green] : [bold yellow]{minutes_left:02d}[/bold yellow] : [blue bold]{seconds_left:02d}[/blue bold]")
        time_elapsed += 1

# Function to clear the console
def clear_console():
    console.clear()

# Function to play Alarm
def play_alarm(sound_file):
    # Load the sound
    sound = pygame.mixer.Sound(sound_file)
    # Play the sound
    sound.play()
    # Wait for the sound to finish playing
    while pygame.mixer.get_busy():
        time.sleep(1)

if __name__ == "__main__":
    main()

# Find a way to play random soothing sounds from online streaming services like YouTube/Spotify.
