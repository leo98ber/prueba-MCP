#!/usr/bin/env python3
"""
Prueba MCP - Módulo principal

Este módulo demuestra funcionalidades básicas
para el proyecto de prueba MCP.
"""

import datetime
from typing import List


class MCPDemo:
    """Clase de demostración para el proyecto MCP"""
    
    def __init__(self, name: str):
        """
        Inicializa la instancia de demostración
        
        Args:
            name (str): Nombre del proyecto
        """
        self.name = name
        self.created_at = datetime.datetime.now()
        self.features = []
    
    def add_feature(self, feature: str) -> None:
        """
        Agrega una nueva funcionalidad
        
        Args:
            feature (str): Descripción de la funcionalidad
        """
        self.features.append({
            'name': feature,
            'added_at': datetime.datetime.now().isoformat()
        })
        print(f"✅ Funcionalidad agregada: {feature}")
    
    def list_features(self) -> List[dict]:
        """
        Lista todas las funcionalidades
        
        Returns:
            List[dict]: Lista de funcionalidades
        """
        return self.features
    
    def get_info(self) -> dict:
        """
        Obtiene información del proyecto
        
        Returns:
            dict: Información completa del proyecto
        """
        return {
            'name': self.name,
            'created_at': self.created_at.isoformat(),
            'features_count': len(self.features),
            'features': self.features
        }


def main():
    """Función principal del programa"""
    print("🤖 Prueba MCP - Demostración")
    print("=" * 40)
    
    # Crear instancia del demo
    demo = MCPDemo("Prueba MCP")
    
    # Agregar funcionalidades
    demo.add_feature("Crear repositorios")
    demo.add_feature("Gestionar ramas")
    demo.add_feature("Crear Pull Requests")
    demo.add_feature("Integración con Claude AI")
    
    # Mostrar información
    print(f"\n📊 Información del proyecto:")
    info = demo.get_info()
    print(f"Nombre: {info['name']}")
    print(f"Creado: {info['created_at']}")
    print(f"Funcionalidades: {info['features_count']}")
    
    print(f"\n📋 Lista de funcionalidades:")
    for i, feature in enumerate(demo.list_features(), 1):
        print(f"{i}. {feature['name']} (agregada: {feature['added_at']})")


if __name__ == "__main__":
    main()
