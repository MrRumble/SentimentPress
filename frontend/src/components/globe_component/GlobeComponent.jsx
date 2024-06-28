import React, { useRef } from 'react';
import { Canvas, useFrame, useLoader } from '@react-three/fiber';
import { Sphere } from '@react-three/drei';
import * as THREE from 'three';
import earthTexture from './globeTexture.png'; // Ensure this path is correct

const Globe = ({ position, scale }) => {
  const globeRef = useRef();
  const texture = useLoader(THREE.TextureLoader, earthTexture);

  useFrame(() => {
    if (globeRef.current) {
      globeRef.current.rotation.x += 0.003; // Adjust rotation speed if needed
    }
  });

  return (
    <Sphere ref={globeRef} args={[1, 32, 32]} position={position} scale={scale}>
      <meshStandardMaterial map={texture} />
    </Sphere>
  );
};

const StaticGlobeBackdrop = () => {
  const globePosition = [0, -3.5, 0]; // Centered globe position
  const globeScale = [3, 3, 3.]; // Adjust scale as needed

  return (
    <div style={{ width: '100%', height: '100vh', position: 'fixed', top: 0, left: 0, zIndex: -1 }}>
      <Canvas
        style={{ width: '100%', height: '100%' }}
        resize={{ polyfill: ResizeObserver }}
      >
        <ambientLight intensity={0.5} />
        <directionalLight position={[5, 5, 5]} />
        <Globe position={globePosition} scale={globeScale} />
      </Canvas>
    </div>
  );
};

export default StaticGlobeBackdrop;
