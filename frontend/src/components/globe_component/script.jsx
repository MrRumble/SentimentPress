import React, { useRef, useEffect } from 'react';
import { Canvas, useFrame, useLoader } from '@react-three/fiber';
import * as THREE from 'three';
import { TextureLoader } from 'three';

const Globe = () => {
    const meshRef = useRef();
    const texture = useLoader(TextureLoader, 'frontend/src/assets/globeTexture.png');

    useFrame(() => {
        if (meshRef.current) {
        // meshRef.current.rotation.y += 0.002;
        meshRef.current.rotation.x += 0.0005;
        }
    });

    return (
        <mesh ref={meshRef} position={[0, -9, 0]}>
        <sphereGeometry args={[10, 100, 100]} />
        <meshBasicMaterial map={texture} />
        </mesh>
    );
    };

    const GlobeScene = () => {
    return (
        <Canvas style={{ background: '#008080', width: '100vw', height: '100vh' }}>
        <perspectiveCamera position={[0, 0, 10]} />
        <ambientLight />
        <Globe />
        </Canvas>
    );
};

export default GlobeScene;
