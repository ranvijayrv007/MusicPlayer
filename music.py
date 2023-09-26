import os
import pygame

class MusicPlayer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.playlist = []
        self.current_track = 0
        self.playing = False

    def add_to_playlist(self, directory):
        if os.path.exists(directory) and os.path.isdir(directory):
            for root, _, files in os.walk(directory):
                for file in files:
                    if file.endswith(".mp3"):
                        self.playlist.append(os.path.join(root, file))
            print("Added all MP3 files in the directory to the playlist.")
        else:
            print("Invalid directory.")

    def play(self):
        if not self.playlist:
            print("Playlist is empty. Add some songs first.")
            return

        if not self.playing:
            pygame.mixer.music.load(self.playlist[self.current_track])
            pygame.mixer.music.play()
            self.playing = True
            print(f"Now playing: {self.playlist[self.current_track]}")

    def pause(self):
        if self.playing:
            pygame.mixer.music.pause()
            self.playing = False
            print("Paused.")

    def resume(self):
        if not self.playing:
            pygame.mixer.music.unpause()
            self.playing = True
            print("Resumed.")

    def next_track(self):
        if self.playing:
            pygame.mixer.music.stop()
            self.current_track = (self.current_track + 1) % len(self.playlist)
            self.play()

    def previous_track(self):
        if self.playing:
            pygame.mixer.music.stop()
            self.current_track = (self.current_track - 1) % len(self.playlist)
            self.play()

    def print_playlist(self):
        for i, track in enumerate(self.playlist):
            print(f"{i+1}. {track}")

if __name__ == "__main__":
    player = MusicPlayer()

    while True:
        print("\nSimple Music Player Menu:")
        print("1. Add songs to the playlist")
        print("2. Play")
        print("3. Pause")
        print("4. Resume")
        print("5. Next track")
        print("6. Previous track")
        print("7. Show playlist")
        print("8. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            directory = input("Enter the directory to add songs: ")
            player.add_to_playlist(directory)
        elif choice == "2":
            player.play()
        elif choice == "3":
            player.pause()
        elif choice == "4":
            player.resume()
        elif choice == "5":
            player.next_track()
        elif choice == "6":
            player.previous_track()
        elif choice == "7":
            player.print_playlist()
        elif choice == "8":
            pygame.mixer.quit()
            pygame.quit()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
