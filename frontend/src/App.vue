<template>
  <main class="container">
    <div class="header">
      <h1>
        Posso comer esse cogumelo? 🍄
      </h1>
      <p>
        Marque as características do seu cogumelo e descubra se ele é comestível 😋 ou venenoso 💀.
      </p>
    </div>
    <div class="itens" :style="{ transform: `translateX(calc(-${controls * 100}% - ${controls}*20px))` }">
      <div class="item">
        <h3> Formato do chapéu</h3>
        <div class="options">
          <div class="option" :class="{ active: output['capShape'] == i.value }" v-for="i in formats" :key="i.name"
            :style="{ backgroundImage: `url(./${i.name}.png)` }" @click="select('capShape', i.value)"><span>
              {{ i.desc }}
            </span>
          </div>
        </div>
      </div>
      <div class="item">
        <h3> Textura da superfície</h3>
        <div class="options">
          <div class="option" :class="{ active: output['capSurface'] == i.value }" v-for="i in surfaces" :key="i.name"
            :style="{ backgroundImage: `url(./${i.name}.png)` }" @click="select('capSurface', i.value)"><span>
              {{ i.desc }}
            </span>
          </div>
        </div>
      </div>
      <div class="item">
        <h3> Cor do chapéu </h3>
        <div class="options">
          <div class="option colors" :class="{ active: output['capColor'] == i.value }" v-for="i in colors"
            :key="i.name" :style="{ backgroundImage: `url(./filter.png)`, backgroundColor: i.name, }"
            @click="select('capColor', i.value)">
            <span>
              {{ i.desc }}
            </span>
          </div>
        </div>
      </div>
      <div class="item">
        <h3>
          Presença de manchas
        </h3>
        <div class="options bruises">
          <div class="option" :class="{ active: output['bruises'] == i.value }" v-for="i in bruises" :key="i.name"
            :style="{ backgroundImage: `url(./${i.name}.png)` }" @click="select('bruises', i.value)">
            <span>
              {{ i.desc }}
            </span>
          </div>
        </div>
      </div>
      <div class="item">
        <h3>Odor característico</h3>
        <div class="options">
          <div class="option" :class="{ active: output['odor'] == i.value }" v-for="i in odors" :key="i.name"
            :style="{ backgroundImage: `url(./${i.name}.png)` }" @click="select('odor', i.value)">
            <span>
              {{ i.desc }}
            </span>
          </div>
        </div>
      </div>
    </div>
    <div class="between">
      <button class="button" :disabled="controls == 0" @click="previous">
        Anterior
      </button>
      <button class="button" :disabled="controls == 4" @click="next">
        Próximo
      </button>
    </div>

    <div class="result" v-if="p != null">
      <h1>
        Resultado:
      </h1>
      <div class="barr">
        <div class="between">
          <label>Comestível</label>
          <label>Venenoso
          </label>
        </div>
        <div class="ind" :class="{ loading }" :style="{ left: `${(p * 100).toFixed(0)}%` }"></div>
      </div>
      <div class="resultado">
        <div v-if="p == 0">
          O cogumelo selecionado é <strong>comestível</strong>! Aproveite sua refeição! 😋
        </div>
        <div v-else-if="p < 1">
          Seu cogumelo tem <strong>{{ (p * 100).toFixed(0) }}%</strong> de chance de ser <strong>venenoso
            💀</strong>.
          <br />É
          melhor não
          arriscar!
        </div>
        <div v-else>
          O seu cogumelo é <strong>venenoso</strong> 💀. Não coma!
        </div>
      </div>

    </div>
    <div class="result" v-else>
      Marque as características, o resultado vai aparecer aqui.
    </div>
  </main>
</template>


<script setup>
import { ref, watch } from 'vue';

const output = ref({
  'capShape': null,
  'capSurface': null,
  'capColor': null,
  bruises: null,
  odor: null
});

const formats = ref([
  { name: 'bell', value: 'b', desc: 'sino' },
  { name: 'conical', value: 'c', desc: 'cone' },
  { name: 'convex', value: 'x', desc: 'convexo' },
  { name: 'flat', value: 'f', desc: 'achatado' },
  { name: 'knobbed', value: 'k', desc: 'protuberante' },
  { name: 'sunken', value: 's', desc: 'afundado' }
]);
const surfaces = ref([
  { name: 'fibrous', value: 'f', desc: 'fibroso' },
  { name: 'grooves', value: 'g', desc: 'sulcada' },
  { name: 'scaly', value: 'y', desc: 'escamosa' },
  { name: 'smooth', value: 's', desc: 'lisa' },
]);

const colors = ref([
  { name: 'brown', value: 'n' },
  { name: '#DAA06D', value: 'b' },
  { name: '#D47E30', value: 'c' },
  { name: 'gray', value: 'g' },
  { name: 'green', value: 'r' },
  { name: 'pink', value: 'p' },
  { name: 'purple', value: 'u' },
  { name: 'red', value: 'e' },
  { name: 'white', value: 'w' },
  { name: '#FBEC5D', value: 'y' }
]);

const bruises = ref([
  { name: 'knobbed', value: 't' },
  { name: 'convex', value: 'f' }
]);

const odors = ref([
  { value: 'a', name: 'almond', desc: 'amêndoa' },
  { value: 'l', name: 'anise', desc: 'anis' },
  { value: 'c', name: 'creosote', desc: 'alcatrão' },
  { value: 'y', name: 'fishy', desc: 'peixe' },
  { value: 'f', name: 'foul', desc: 'fétido' },
  { value: 'm', name: 'musty', desc: 'mofo' },
  { value: 'n', name: 'none', desc: 'nenhum' },
  { value: 'p', name: 'pungent', desc: 'ardido' },
  { value: 's', name: 'spicy', desc: 'especiado' },
]);

const select = (key, value) => {
  output.value[key] = value;
}

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

const p = ref(null);
const loading = ref(true)

watch(() => output.value, async () => {

  const all = Object.values(output.value).every(i => i)
  if (!all) return
  loading.value = true

  let params = new URLSearchParams()
  Object.entries(output.value).forEach(([k, v]) => {
    params.set(k, v)
  })
  try {
    const res = await fetch(`http://localhost:5000/classify?${params}`, {
      method: 'GET'
    })
    const value = await res.json()

    p.value = value.result.p
    loading.value = false
  } catch (error) {

  }
}, { deep: true })
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Pixelify+Sans:wght@400..700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&family=Pixelify+Sans:wght@400..700&display=swap');

* {
  box-sizing: border-box;
}

h1 {
  margin-block: 1rem;
  font-size: 3rem;
}

label {
  font-size: 1.5rem;
  padding-inline: 1rem;
  margin-top: -0.5rem;
  z-index: 1;
  font-family: 'Pixelify Sans', sans-serif;
  color: #0b4018;
  font-weight: 800;

  &:first-of-type {
    color: white;
  }

}

body {
  background-image: url('./bg.png');
  background-color: #0b201076;
  background-blend-mode: overlay;
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

h3 {
  font-weight: 500;
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
  width: 1200px;
}



.itens {
  transition: all 0.3s ease-in-out;
  display: flex;
  align-items: center;
  max-width: 1200px;
  gap: 20px;
}

.item {
  height: -webkit-fill-available;
  height: -moz-available;
  background-color: rgba(0, 0, 0, 0.223);
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
  background-color: rgba(255, 255, 255, 0.597);
  backdrop-filter: blur(100px);
  background-size: cover;
  background-position: center;
  width: 200px;
  height: 200px;
  cursor: pointer;
  display: flex;
  align-items: flex-end;
  justify-content: flex-start;

  &.colors {
    width: 150px;
    background-blend-mode: multiply;
    height: 150px;
  }

  &.active {
    outline: 4px solid #d5d5d5;
    outline-offset: 4px;
  }

  span {
    background-image: url('./filter.png');
    background-color: #0b4018;
    background-blend-mode: multiply;
    background-size: cover;
    background-position: center;
    color: rgb(203, 202, 201);
    padding: 0.25rem 0.5rem;

  }
}

.between {
  display: flex;
  justify-content: space-between;
  margin-block: 20px;
}

.barr {
  background: #1cff14;
  background: linear-gradient(90deg, rgba(69, 100, 255, 1) 0%, rgba(87, 199, 133, 1) 32%, rgba(28, 255, 20, 1) 100%);
  height: 20px;
  position: relative;
  margin: 40px;

  &:before,
  &:after {
    content: '';
    background: #1cff14;
    background: linear-gradient(90deg, rgba(69, 100, 255, 1) 0%, rgba(87, 199, 133, 1) 32%, rgba(28, 255, 20, 1) 100%);
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

  .ind {
    position: absolute;
    top: -40px;
    margin-left: -50px;
    width: 100px;
    height: 100px;
    background-image: url('./bell.png');
    transition: all 0.3s ease-in-out;
    background-size: cover;
    background-position: center;
    z-index: 1;

    &.loading {
      opacity: 0.5;
      animation: bounce 0.2s ease-in-out infinite;
    }
  }
}

.resultado {
  margin-top: 1rem;
  margin-bottom: 4rem;
  min-height: 2rem;
  text-align: center;
  font-size: 2rem;
}

@keyframes bounce {

  0%,
  100% {
    transform: rotate(5deg);
    animation-timing-function: cubic-bezier(0.8, 0, 1, 1);
  }

  50% {
    transform: none;
    animation-timing-function: cubic-bezier(0, 0, 0.2, 1);
  }
}
</style>
