from manim import*

class conjuntos(MovingCameraScene):
    def construct(self):
        
     
        self.camera.background_color = WHITE



#logo nao está funcionando - corrigir
        try:
            img = ImageMobject('logounivasfbranca').scale(0.2)
            img.to_corner(DR, buff = 0.1)
            self.add_fixed_in_frame_mobjects(img)
        except:
            print('LOGO NAO ENCONTRADA')

        titulo = Tex(r"Conjuntos Numéricos", color = BLACK).scale(1.2).move_to(ORIGIN)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))


    #construindo elipses
        N_elipse = Ellipse(width=4, height=2, color=PURE_GREEN, stroke_width=4).set_z_index(5)
        Z_elipse = Ellipse(width=7, height=3.5, color=PURE_RED, stroke_width=4).set_z_index(4)
        Q_elipse = Ellipse(width=10, height=5, color=PURE_BLUE, stroke_width=4).set_z_index(2)
        R_elipse = Ellipse(width=13, height=6.5, color=PINK, stroke_width=4).set_z_index(3)
        

    #construindo rótulos
        N_label = MathTex(r'\mathbb{N}').set_color(PURE_GREEN).scale(0.5).next_to(N_elipse, RIGHT)
        Z_label = MathTex(r'\mathbb{Z}').set_color(PURE_RED).scale(0.5).next_to(Z_elipse, RIGHT)
        R_label = MathTex(r'\mathbb{R}').set_color(PINK).scale(0.5).next_to(R_elipse, RIGHT)
        Q_label = MathTex(r'\mathbb{Q}').set_color(PURE_BLUE).scale(0.5).next_to(Q_elipse, RIGHT)


    #criando exemplo de número em cada conjunto

        N_num = Tex(r'\{0, 1, 2, 3, ...\}').set_color(PURE_GREEN).scale(0.7).move_to(N_elipse.get_center())    
        Z_num = Tex(r'\{..., -2, -1, 0, 1, 2, ...\}').set_color(PURE_RED).scale(0.7).move_to(Z_elipse.get_center()+ DOWN*1.2)
        Q_num = Tex(r'\{ ...-2, -1/2,  -1,  1/2, 2...\}').set_color(PURE_BLUE).scale(0.7).move_to(Q_elipse.get_center()+DOWN*2)
        R_num = MathTex(r'\{ ...-2, -\sqrt{2}, -1, 0, 1, \sqrt{2}, 2...\}').set_color(PINK).scale(0.7).move_to(R_elipse.get_center()+DOWN*2.8)


    #iniciando animação - N
        
        self.camera.frame.save_state()
        self.camera.frame.set(width=8)  

        self.play(Create(N_elipse), Write(N_label), Write(N_num))
        self.wait()
        
        


    #Z

        self.play(
            self.camera.frame.animate.set(width=10),
            run_time = 2
        )
        self.play(Create(Z_elipse), Write(Z_label), Write(Z_num))
        self.wait()
        
        


     #Q
        self.play(
            self.camera.frame.animate.set(width=16),
            run_time = 2
        )
        self.play(Create(Q_elipse), Write(Q_label), Write(Q_num))
        self.wait()
        
          


    #R
        self.play(
            self.camera.frame.animate.set(width=18),
            run_time = 2
        )
        self.play(Create(R_elipse), Write(R_label), Write(R_num))
        self.wait(3)


        #fadeout geral
        self.play(
            FadeOut(N_elipse), FadeOut(N_label), FadeOut(N_num),
            FadeOut(Z_elipse), FadeOut(Z_label), FadeOut(Z_num),
            FadeOut(Q_elipse), FadeOut(Q_label), FadeOut(Q_num),
            FadeOut(R_elipse), FadeOut(R_label), FadeOut(R_num)
        )
        self.camera.frame.animate.set(width=14)
        self.wait()

                    
  

       



        

