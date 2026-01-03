"""
Tests for the Anti-Gravity Simulator
"""

import pytest
import numpy as np
from src.simulator import AntiGravitySimulator, AntiGravityField

def test_field_initialization():
    """Test that field initializes with correct defaults"""
    field = AntiGravityField()
    assert field.strength == 0.8
    assert field.frequency == 9.8
    assert field.radius == 5.0
    assert field.stability == 0.95

def test_field_validation():
    """Test field parameter validation"""
    with pytest.raises(ValueError):
        AntiGravityField(strength=1.5)  # Invalid strength
    
    with pytest.raises(ValueError):
        AntiGravityField(stability=-0.1)  # Invalid stability

def test_simulator_initialization():
    """Test simulator initialization"""
    simulator = AntiGravitySimulator(mass=10.0)
    assert simulator.mass == 10.0
    assert simulator.field.strength == 0.8

def test_force_calculation():
    """Test anti-gravity force calculation"""
    simulator = AntiGravitySimulator(mass=1.0)
    
    # Force should be between -1 and 1
    force = simulator.calculate_force(time=0.5)
    assert -1.0 <= force <= 1.0
    
    # Force should vary with time
    force1 = simulator.calculate_force(time=0.0)
    force2 = simulator.calculate_force(time=0.1)
    assert force1 != force2

def test_trajectory_simulation():
    """Test trajectory simulation"""
    simulator = AntiGravitySimulator(mass=5.0)
    times, heights = simulator.simulate_trajectory(duration=2.0, steps=10)
    
    assert len(times) == 10
    assert len(heights) == 10
    assert times[0] == 0.0
    assert times[-1] == 2.0

def test_optimization():
    """Test field optimization"""
    simulator = AntiGravitySimulator(mass=1.0)
    optimized = simulator.optimize_field(target_height=15.0)
    
    # Optimized strength should be >= original
    assert optimized.strength >= simulator.field.strength
    # Should not exceed 1.0
    assert optimized.strength <= 1.0

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
