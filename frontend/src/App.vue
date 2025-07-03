<template>
  <main class="container">
    <div class="header">
      <h1>
        Posso comer esse cogumelo?
      </h1>
      <p>
        Escolha as características do cogumelo e descubra se ele é comestível ou não.
      </p>
    </div>
    <div class="itens" :style="{ transform: `translateX(calc(-${controls * 100}% - ${controls}*20px))` }">
      <div class="item">
        Formato do chapéu
        <div class="options">
          <div class="option" :class="{ active: output['cap-shape'] == i.value }" v-for="i in formats" :key="i.name"
            :style="{ backgroundImage: `url(./${i.name}.png)` }" @click="output['cap-shape'] = i.value">
          </div>
        </div>
      </div>
      <div class="item">
        Textura da superfície<div class="options">
          <div class="option" :class="{ active: output['cap-surface'] == i.value }" v-for="i in surfaces" :key="i.name"
            :style="{ backgroundImage: `url(./${i.name}.png)` }" @click="output['cap-surface'] = i.value">
          </div>
        </div>
      </div>
      <div class="item">
        Cor do chapéu<div class="options">
          <div class="option bell"></div>
          <div class="option bell"></div>
          <div class="option bell"></div>
          <div class="option bell"></div>
          <div class="option bell"></div>
          <div class="option bell"></div>
          <div class="option bell"></div>
          <div class="option bell"></div>
          <div class="option bell"></div>
          <div class="option bell"></div>
        </div>
      </div>
      <div class="item">
        Presença de manchas<div class="options">
          <div class="option bell"></div>
          <div class="option bell"></div>

        </div>
      </div>
      <div class="item">
        Odor característico<div class="options">
          <div class="option bell"></div>
          <div class="option bell"></div>
          <div class="option bell"></div>
          <div class="option bell"></div>
          <div class="option bell"></div>
          <div class="option bell"></div>
          <div class="option bell"></div>
          <div class="option bell"></div>
          <div class="option bell"></div>
        </div>
      </div>
    </div>
    <div class="between">
      <button class="button" @click="previous">
        Anterior
      </button>
      <button class="button" @click="next">
        Próximo
      </button>
    </div>

    <div class="result">
      <h1>
        Resultado:
      </h1>
      <div class="between">
        <div>Venenoso</div>
        <div>Comestível</div>
      </div>
      <div class="barr"></div>
      <div class="resultado">
        <template v-if="p != null">

          <div v-if="p == 0">
            O cogumelo selecionado é <strong>comestível</strong>! Aproveite sua refeição!
          </div>
          <div v-else-if="p < 1">
            Há uma chance de <strong>{{ (p * 100).toFixed(0) }}%</strong> do cogumelo ser venenoso. É melhor não
            arriscar!
          </div>
          <div v-else>
            O cogumelo selecionado é <strong>venenoso</strong>. Evite consumi-lo!
          </div>
        </template>
      </div>

    </div>
  </main>
</template>


<script setup>
import { ref } from 'vue';

const output = ref({
  'cap-shape': null,
  'cap-surface': null,
  'cap-color': null,
  bruises: null,
  odor: null
});

const formats = ref([
  { name: 'bell', value: 'b' },
  { name: 'conical', value: 'c' },
  { name: 'convex', value: 'x' },
  { name: 'flat', value: 'f' },
  { name: 'knobbed', value: 'k' },
  { name: 'sunken', value: 's' }
]);
const surfaces = ref([
  { name: 'fibrous', value: 'f' },
  { name: 'grooves', value: 'g' },
  { name: 'scaly', value: 'y' },
  { name: 'smooth', value: 's' },
]);

const colors = ref([
  { name: 'brown', value: 'n' },
  { name: 'buff', value: 'b' },
  { name: 'cinnamon', value: 'c' },
  { name: 'gray', value: 'g' },
  { name: 'green', value: 'r' },
  { name: 'pink', value: 'p' },
  { name: 'purple', value: 'u' },
  { name: 'red', value: 'e' },
  { name: 'white', value: 'w' },
  { name: 'yellow', value: 'y' }
]);

const controls = ref((0))

const next = () => {
  if (controls.value < 4) {
    controls.value += 1;
  }
};

const previous = () => {
  if (controls.value > 0) {
    controls.value -= 1;
  }
};

const p = ref(0.5);
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
  min-height: 100vh;
  overflow-x: hidden;
}

h1 {
  font-family: 'Pixelify Sans', sans-serif;
}

.blur {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  z-index: 0;
  background-color: rgba(90, 90, 90, 0.1);
  backdrop-filter: blur(10px);
}

#app {
  display: flex;
  /* align-self: start; */
}

main.container {
  display: flex;
  flex-direction: column;
  margin-inline-start: 50vw;
  transform: translateX(-50%);
  width: 1000px;
}



.itens {
  transition: all 0.3s ease-in-out;
  display: flex;
  align-items: center;
  margin-top: 20px;
  max-width: 1000px;
  gap: 20px;
}

.item {
  background-color: rgba(0, 0, 0, 0.123);
  border: 0.1px solid rgba(36, 36, 36, 0.2);
  border-top: 0.1px solid rgba(255, 255, 255, 0.2);
  border-radius: 10px;
  padding: 2rem;
  flex: auto;
  margin: 1rem 0;
  text-align: center;
  font-family: 'Pixelify Sans', sans-serif;
  font-size: 24px;
  backdrop-filter: blur(10px);
  min-width: 100%;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.options {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  gap: 20px;
}

.option {
  background-color: rgba(173, 173, 173, 0.1);
  backdrop-filter: blur(100px);
  background-size: cover;
  background-position: center;
  width: 200px;
  height: 200px;
  cursor: pointer;

  &.active {
    outline: 4px solid #d5d5d5;
    outline-offset: 4px;
  }
}

.conical {
  background-image: url('./conical.png');
}

.bell {
  background-image: url('./bell.png');
}

.between {
  display: flex;
  justify-content: space-between;
  margin-block: 20px;
}

.barr {
  background: #1cff14;
  background: linear-gradient(90deg, rgba(28, 255, 20, 1) 0%, rgba(87, 199, 133, 1) 32%, rgba(69, 100, 255, 1) 100%);
  height: 20px;
  position: relative;

  &:before,
  &:after {
    content: '';
    background: #1cff14;
    background: linear-gradient(90deg, rgba(28, 255, 20, 1) 0%, rgba(87, 199, 133, 1) 32%, rgba(69, 100, 255, 1) 100%);
    height: 10px;
    width: calc(100% - 20px);
    position: absolute;
    left: 10px;
  }

  &:before {
    top: -10px;
  }

  &:after {
    top: 20px;
  }
}

.resultado {
  margin-top: 1rem;
  min-height: 2rem;
}
</style>
