<template>

  <main class="container">
    <h1>
      Posso comer esse cogumelo?
    </h1>
    <p>
      Escolha as características do cogumelo e descubra se ele é comestível ou não.
    </p>
    <div class="itens">

      <div class="item">
        Formato do chapéu
        <div class="options">

          <div class="option bell"></div>
          <div class="option">B</div>
          <div class="option">C</div>
        </div>
      </div>
      <div class="item">
        Textura da superfície
      </div>
      <div class="item">
        Cor do chapéu
      </div>
      <div class="item">
        Presença de manchas
      </div>
      <div class="item">
        Odor característico
      </div>
    </div>
  </main>
</template>


<script setup>
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Pixelify+Sans:wght@400..700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&family=Pixelify+Sans:wght@400..700&display=swap');

* {
  box-sizing: border-box;
}

body {
  background-image: url('./bg.png');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  color: #fff;
  font-size: 20px;
  font-family: 'Montserrat', sans-serif;

}

h1 {
  font-family: 'Pixelify Sans', sans-serif;
}

.blur {
  position: absolute;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: 0;
  background-color: rgba(90, 90, 90, 0.1);
  backdrop-filter: blur(10px);
}

main.container {
  position: fixed;
  z-index: 0;
  top: 0;
  left: 0;
  height: 100vh;
  width: 100vw;
  margin-block: 100px;
  padding: 0 8vw;
}

.itens {
  display: flex;
  align-items: center;
  gap: 20px;
  margin-top: 20px;
}

.item {
  background-color: rgba(150, 150, 150, 0);
  border: 0.1px solid rgba(36, 36, 36, 0.2);
  border-top: 0.1px solid rgba(255, 255, 255, 0.2);
  border-radius: 10px;
  padding: 20px;
  flex: auto;
  margin: 10px auto;
  text-align: center;
  font-family: 'Pixelify Sans', sans-serif;
  font-size: 24px;
  backdrop-filter: blur(10px);
  min-width: 100%;

}

.options {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
}

.bell {
  background-image: url('./bell.png');
  background-size: cover;
  background-position: center;
  width: 150px;
  height: 150px;
}
</style>
