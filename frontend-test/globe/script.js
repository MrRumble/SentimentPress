// Set up scene, camera, and renderer
var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
var renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.getElementById('container').appendChild(renderer.domElement);


// Set background color
renderer.setClearColor(0x008080); // Set to black or any other hexadecimal color value

document.getElementById('container').appendChild(renderer.domElement);

// Create a sphere geometry
var geometry = new THREE.SphereGeometry(10, 100, 100);

// Load a texture for the globe (replace with your own globe texture)
var textureLoader = new THREE.TextureLoader();
var texture = textureLoader.load('/frontend/globe/globeTexture.png');

// Apply the texture to the material
var material = new THREE.MeshBasicMaterial({ map: texture });

// Create a mesh with geometry and material, and add to the scene
var globe = new THREE.Mesh(geometry, material);
scene.add(globe);

// Set camera position
camera.position.z = 10;
globe.position.set(0, -9, 0);

// Function to animate the globe
function animate() {
    requestAnimationFrame(animate);
    // globe.rotation.y += 0.002;
    globe.rotation.x += 0.0005;
    renderer.render(scene, camera);
}

// Call animate function to start the animation loop
animate();
