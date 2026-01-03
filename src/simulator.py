"""
Anti-Gravity Simulator - Core Physics Engine
"""

import numpy as np
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class AntiGravityField:
    """Represents an anti-gravity field configuration"""
    strength: float = 0.8      # Field strength (0.0 to 1.0)
    frequency: float = 9.8     # Oscillation frequency (Hz)
    radius: float = 5.0        # Field radius (meters)
    stability: float = 0.95    # Field stability (0.0 to 1.0)
    
    def __post_init__(self):
        """Validate field parameters"""
        if not 0.0 <= self.strength <= 1.0:
            raise ValueError("Field strength must be between 0.0 and 1.0")
        if not 0.0 <= self.stability <= 1.0:
            raise ValueError("Stability must be between 0.0 and 1.0")

class AntiGravitySimulator:
    """Main simulator class"""
    
    def __init__(self, mass: float = 1.0):
        """
        Initialize simulator with object mass
        
        Args:
            mass: Mass of object in kilograms
        """
        self.mass = mass
        self.field = AntiGravityField()
        self.time = 0.0
        
    def calculate_force(self, time: float = None) -> float:
        """
        Calculate anti-gravity force at given time
        
        Args:
            time: Time in seconds (uses internal time if None)
            
        Returns:
            Force in Newtons (positive = upward, negative = downward)
        """
        if time is None:
            time = self.time
            self.time += 0.1  # Auto-increment for animation
        
        # Core physics equation: F = strength * sin(2π * frequency * time) * stability
        force = (self.field.strength * 
                np.sin(2 * np.pi * self.field.frequency * time) * 
                self.field.stability)
        
        # Adjust for mass (heavier objects need more force)
        adjusted_force = force * (1 / (1 + 0.1 * self.mass))
        
        return round(adjusted_force, 4)
    
    def simulate_trajectory(self, duration: float = 10.0, steps: int = 100) -> Tuple[List[float], List[float]]:
        """
        Simulate object trajectory over time
        
        Args:
            duration: Simulation duration in seconds
            steps: Number of time steps
            
        Returns:
            (time_points, height_points) - trajectory data
        """
        time_points = np.linspace(0, duration, steps)
        height_points = []
        current_height = 0.0
        velocity = 0.0
        
        for t in time_points:
            force = self.calculate_force(t)
            # Simple physics: F = ma, then integrate for velocity and position
            acceleration = force / self.mass
            velocity += acceleration * (duration / steps)
            current_height += velocity * (duration / steps)
            height_points.append(current_height)
            
        return time_points.tolist(), height_points
    
    def optimize_field(self, target_height: float = 10.0) -> AntiGravityField:
        """
        Optimize field parameters to reach target height
        
        Args:
            target_height: Desired levitation height in meters
            
        Returns:
            Optimized field configuration
        """
        # Simple optimization: increase strength for higher target
        optimized_strength = min(1.0, self.field.strength * (1 + target_height * 0.05))
        
        optimized_field = AntiGravityField(
            strength=optimized_strength,
            frequency=self.field.frequency,
            radius=self.field.radius,
            stability=max(0.8, self.field.stability)
        )
        
        return optimized_field
