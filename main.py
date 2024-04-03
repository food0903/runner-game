import pygame

pygame.init()
screen = pygame.display.set_mode((500, 700))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
game_active = False
start_time = 0

def display_score():
  current_time = str(int(pygame.time.get_ticks() / 1000 - start_time))
  score_surface = test_font.render('Score: ' + current_time, False, 'Black')
  score_rect = score_surface.get_rect(center = (250, 50))
  screen.blit(score_surface, score_rect)
  return current_time

score = 0
  
# Background
sky_surface = pygame.image.load(
    'assets/platformerGraphics_mushroomLand/Backgrounds/bg_grasslands.png')
sky_surface = pygame.transform.scale(sky_surface, (500, 700)).convert_alpha()



snail_surface = pygame.image.load(
    'assets/platformerGraphicsDeluxe_Updated/Enemies/snailWalk1.png'
).convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(570, 630))

player_surface = pygame.image.load(
    'assets/platformerGraphicsDeluxe_Updated/Player/p1_walk/PNG/p1_walk08.png'
).convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 630))
player_gravity = 0

# Intro screen
player_stand = pygame.image.load('assets/platformerGraphicsDeluxe_Updated/Player/p1_walk/PNG/p1_walk08.png').convert_alpha()
player_stand = pygame.transform.scale(player_stand, (200, 200)).convert_alpha()
player_stand_rect = player_stand.get_rect(center = (250, 350))

grass_surface = pygame.image.load(
    'assets/platformerGraphicsDeluxe_Updated/Tiles/grassHalf.png'
).convert_alpha()

# Calculate the number of grass tiles needed to fill the screen width
num_grass_tiles = screen.get_width() // grass_surface.get_width() + 1

# Create a list of grass rectangles
grass_rects = [
    grass_surface.get_rect(midtop=(x * grass_surface.get_width() +
                                   grass_surface.get_width() // 2, 630))
    for x in range(num_grass_tiles)
]

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
    if game_active:
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE and player_rect.bottom >= 630:
          player_gravity = -20
      if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 630:
        player_gravity = -20
    else:
      if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or event.type == pygame.MOUSEBUTTONDOWN:
        game_active = True
        snail_rect.x = 570
        start_time = int(pygame.time.get_ticks()/1000)
  if game_active:
    screen.blit(sky_surface, (0, 0))
    score = display_score()
    snail_rect.x -= 6
  
    if snail_rect.right <= -50:
      snail_rect.left = 500
  
    for grass_rect in grass_rects:
      screen.blit(grass_surface, grass_rect)
  
    screen.blit(snail_surface, snail_rect)
  
    #player
    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 630:
      player_rect.bottom = 630
    screen.blit(player_surface, player_rect)
    
    if player_rect.colliderect(snail_rect):
      game_active = False
  else:
    

    screen.fill((223,255,0))
    screen.blit(player_stand, player_stand_rect)
    score_message = test_font.render(f'Your score: {score}', False, 'Black')
    screen.blit(score_message, (player_stand_rect.x, player_stand_rect.bottom + 100 ))
    welcome_message = test_font.render('hit [space] to start', False, 'Black')
    screen.blit(welcome_message, (player_stand_rect.x-45, player_stand_rect.top - 100 ))
    
    

  pygame.display.update()
  clock.tick(60)
