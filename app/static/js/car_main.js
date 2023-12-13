// const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

const loader = new THREE.GLTFLoader();

loader.load('model.glb', (gltf) => {
  const model = gltf.scene;
  scene.add(model);

  const animate = () => {
    requestAnimationFrame(animate);
    model.rotation.y += 0.01;
    renderer.render(scene, camera);
  };

  animate();
}, undefined, (error) => {
  console.error('An error occurred:', error);
});

const light = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(light);

camera.position.z = 5;

function onWindowResize() {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
}

window.addEventListener('resize', onWindowResize, false);
