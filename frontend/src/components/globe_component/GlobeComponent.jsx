import React, { useRef, useEffect } from 'react';
import * as THREE from 'three';

const Globe = () => {
  const globeRef = useRef();

  useEffect(() => {
    let scene, camera, renderer, globe;

    // Set up scene
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    globeRef.current.appendChild(renderer.domElement);

    // Create globe geometry
    const geometry = new THREE.SphereGeometry(5, 32, 32);
    const texture = new THREE.TextureLoader().load('./globeTexture.png'); // Adjust path as necessary
    const material = new THREE.MeshBasicMaterial({ map: texture });
    globe = new THREE.Mesh(geometry, material);
    scene.add(globe);

    // Set up animation
    const animate = () => {
      requestAnimationFrame(animate);
      globe.rotation.y += 0.005;
      renderer.render(scene, camera);
    };

    // Resize handler
    const handleResize = () => {
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    };

    window.addEventListener('resize', handleResize);

    // Clean up
    return () => {
      window.removeEventListener('resize', handleResize);
      globeRef.current.removeChild(renderer.domElement);
    };

    // Start animation
    animate();

  }, []);

  return (
    <div style={{ width: '100%', height: '100%' }} ref={globeRef} />
  );
};

export default Globe;
