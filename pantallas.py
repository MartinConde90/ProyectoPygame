import pygame as pg






class Inicial(pg.sprite.Sprite):
    while True:
            self.screen.blit(self.background_imga,(0,0))
            self.screen.blit(self.text_titulo,(100,100))
            self.screen.blit(self.text_insert_coin,(235,350)) 
            
            pg.display.update()
            for event in pg.event.get():
                if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            self.mainloop()
                            
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_s:
                        main_loop()
                        
                if event.type == QUIT:
                        pg.quit()
                        sys.exit()