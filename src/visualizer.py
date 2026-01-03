"""
Visualization module for anti-gravity simulations
"""

import matplotlib.pyplot as plt
import numpy as np
from typing import List, Tuple
from .simulator import AntiGravitySimulator

class AntiGravityVisualizer:
    """Create visualizations of anti-gravity simulations"""
    
    @staticmethod
    def plot_trajectory(time_points: List[float], height_points: List[float], 
                        save_path: str = None):
        """
        Plot object trajectory over time
        
        Args:
            time_points: List of time values
            height_points: List of height values
            save_path: Optional path to save the plot
        """
        plt.figure(figsize=(10, 6))
        plt.plot(time_points, height_points, 'b-', linewidth=2, label='Trajectory')
        plt.fill_between(time_points, height_points, alpha=0.2, color='blue')
        
        plt.xlabel('Time (seconds)', fontsize=12)
        plt.ylabel('Height (meters)', fontsize=12)
        plt.title('Anti-Gravity Levitation Trajectory', fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.3)
        plt.legend()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"Plot saved to {save_path}")
        
        plt.show()
    
    @staticmethod
    def plot_field_strength(simulator: AntiGravitySimulator, duration: float = 5.0):
        """
        Visualize anti-gravity field strength over time
        
        Args:
            simulator: AntiGravitySimulator instance
            duration: Time duration to visualize
        """
        time_points = np.linspace(0, duration, 200)
        forces = [simulator.calculate_force(t) for t in time_points]
        
        plt.figure(figsize=(10, 6))
        plt.plot(time_points, forces, 'r-', linewidth=2, label='Field Force')
        
        # Add zero line for reference
        plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        
        plt.xlabel('Time (seconds)', fontsize=12)
        plt.ylabel('Force (Newtons)', fontsize=12)
        plt.title('Anti-Gravity Field Oscillation', fontsize=14, fontweight='bold')
        plt.grid(True, alpha=0.3)
        plt.legend()
        
        plt.show()
    
    @staticmethod
    def create_3d_field(simulator: AntiGravitySimulator):
        """Create 3D visualization of anti-gravity field"""
        try:
            from mpl_toolkits.mplot3d import Axes3D
            
            x = np.linspace(-simulator.field.radius, simulator.field.radius, 30)
            y = np.linspace(-simulator.field.radius, simulator.field.radius, 30)
            X, Y = np.meshgrid(x, y)
            
            # Field strength decreases with distance from center
            R = np.sqrt(X**2 + Y**2)
            Z = simulator.field.strength * np.exp(-R**2) * np.sin(R * 2 * np.pi)
            
            fig = plt.figure(figsize=(12, 8))
            ax = fig.add_subplot(111, projection='3d')
            surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
            
            ax.set_xlabel('X (meters)')
            ax.set_ylabel('Y (meters)')
            ax.set_zlabel('Field Strength')
            ax.set_title('3D Anti-Gravity Field Visualization')
            
            fig.colorbar(surf, shrink=0.5, aspect=5)
            plt.show()
            
        except ImportError:
            print("3D visualization requires matplotlib 3D toolkit")
