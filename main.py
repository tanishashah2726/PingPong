import asyncio
import pygame.event

from settings import *
from sprites import *
from groups import AllSprites
import json

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption("Pong")
        self.clock = pygame.time.Clock()
        self.running = True

        #sprites
        self.all_sprites = AllSprites()
        self.paddle_sprites = pygame.sprite.Group()
        self.player = Player((self.all_sprites,self.paddle_sprites))
        self.ball = Ball(self.all_sprites,self.paddle_sprites, self.update_score)
        Opponent((self.all_sprites,self.paddle_sprites), self.ball)

        #score
        try:
            with open(join('data', 'score.txt')) as score_file:
                self.score = json.load(score_file)
        except:
            self.score = {'player':0, 'opponent':0}
        self.font = pygame.font.Font(None, 160)

    def display_score(self):
        #player
        player_surf = self.font.render(str(self.score['player']), True, COLORS['bg detail'])
        player_rect = player_surf.get_frect(center=(WINDOW_WIDTH / 2 + 100, WINDOW_HEIGHT / 2))
        self.display_surface.blit(player_surf, player_rect)

        #opponent
        opponent_surf = self.font.render(str(self.score['opponent']), True, COLORS['bg detail'])
        opponent_rect = opponent_surf.get_frect(center=(WINDOW_WIDTH / 2 - 100, WINDOW_HEIGHT / 2))
        self.display_surface.blit(opponent_surf, opponent_rect)

        #line seperator
        pygame.draw.line(self.display_surface, COLORS['bg detail'], (WINDOW_WIDTH/2, 0), (WINDOW_WIDTH/2, WINDOW_HEIGHT), 10)

    def update_score(self, side):
        if side == 'player':
            self.score['player'] += 1
            SPEED['opponent'] += 25
        else:
            self.score['opponent'] += 1
            SPEED['opponent'] -= 25

        if SPEED['opponent'] >= 350:
            SPEED['opponent'] = 300

        if self.score['player'] >= 15 or self.score['opponent'] >= 15:
            self.score['player'] = 0
            self.score['opponent'] = 0
            SPEED['opponent'] = 175

        self.reverse_player()

    def reverse_player(self):
        if self.score['player'] >=10:
            REVERSE['player'] = -1
        else:
            REVERSE['player'] = 1

    async def run(self):
        while self.running:
            dt=self.clock.tick()/1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    SPEED['opponent'] = 175
                    self.running = False
                    try:
                        with open(join('data', 'score.txt'), 'w') as score_file:
                            json.dump(self.score, score_file)
                    except:
                        pass

            #update
            self.all_sprites.update(dt)

            #drawing
            self.display_surface.fill(COLORS['bg'])
            self.display_score()
            self.all_sprites.draw()
            pygame.display.update()

            await asyncio.sleep(0)

        pygame.quit()

async def main():
    game=Game()
    await game.run()

if __name__ == "__main__":
    asyncio.run(main())