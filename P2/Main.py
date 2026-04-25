from Pokemon import Pokemon
from SuperHero import SuperHero
from Weather import Weather

class Main:
    def _init_(self):
        self.pokemon_service = Pokemon()
        self.hero_service = SuperHero()
        self.weather_service = Weather()

    def menu(self):
        print("-" * 50)
        print("WEB SERVICE INFORMATION CENTER")
        print("-" * 50)
        print()

        # Input
        favorite_pokemon = input("Enter your favorite Pokemon: ").strip().lower()
        favorite_hero = input("Enter your favorite Super Hero: ").strip()
        city = input("Enter your city of residence: ").strip()

        print("\n" + "-" * 50)
        print("INFORMATION...")
        print("-" * 50)

        # Pokemon
        print("-" * 40)
        print("POKEMON INFORMATION")
        print("-" * 40)
        self._get_pokemon_info(favorite_pokemon)

        print()

        # Super Hero
        print("-" * 40)
        print("SUPER HERO INFORMATION")
        print("-" * 40)
        self._get_hero_info(favorite_hero)

        print()

        # Weather
        print("-" * 40)
        print("WEATHER INFORMATION")
        print("-" * 40)
        self._get_weather_info(city)


    def _get_pokemon_info(self, pokemon_name):
        try:
            if not pokemon_name:
                print("Error: No Pokemon name provided.")
                return

            # This now prints info AND returns the sprite URL
            sprite_url = self.pokemon_service.get_pokemon(pokemon_name)

            if sprite_url:
                file_name = f"{pokemon_name}.png"
                self.pokemon_service.get_image(sprite_url, file_name)
            else:
                print(f"Error: Could not retrieve data for '{pokemon_name}'")

        except Exception as e:
            print(f"Error fetching Pokemon information: {e}")


    def _get_hero_info(self, hero_name):
        try:
            if not hero_name:
                print("Error: No hero name provided.")
                return

            result = self.hero_service.get_heroes(hero_name)

            if result is None:
                print(f"Could not retrieve data for '{hero_name}'")

        except Exception as e:
            print(f"Error fetching hero information: {e}")


    def _get_weather_info(self, city):
        try:
            if not city:
                print("Error: No city provided.")
                return
            
            result = self.weather_service.get_weather(city)
            if not result:
                print(f"Could not retrieve weather data for '{city}'")

        except Exception as e:
            print(f"Error fetching weather information: {e}")

if __name__ == "_main_":
    app = Main()
    app.menu()