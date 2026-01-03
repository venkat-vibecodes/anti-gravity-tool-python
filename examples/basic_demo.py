"""
Basic demonstration of the Anti-Gravity Simulator
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.simulator import AntiGravitySimulator
from src.visualizer import AntiGravityVisualizer

def main():
    """Run a complete demonstration"""
    print("=" * 60)
    print("🛸 ANTI-GRAVITY SIMULATOR DEMONSTRATION")
    print("=" * 60)
    
    # Create simulator with 5kg object
    print("\n1. Initializing simulator with 5kg object...")
    simulator = AntiGravitySimulator(mass=5.0)
    
    # Test single force calculation
    print("\n2. Calculating anti-gravity force at t=1.0s...")
    force = simulator.calculate_force(time=1.0)
    print(f"   Force: {force} Newtons")
    
    # Simulate trajectory
    print("\n3. Simulating 10-second trajectory...")
    time_points, height_points = simulator.simulate_trajectory(duration=10.0)
    
    # Show results
    print(f"   Final height after 10 seconds: {height_points[-1]:.2f} meters")
    print(f"   Maximum height reached: {max(height_points):.2f} meters")
    
    # Optimize for higher levitation
    print("\n4. Optimizing field for 20-meter levitation...")
    optimized_field = simulator.optimize_field(target_height=20.0)
    print(f"   Optimized field strength: {optimized_field.strength:.3f}")
    print(f"   Field stability: {optimized_field.stability:.3f}")
    
    # Create visualizations
    print("\n5. Generating visualizations...")
    
    # Plot 1: Trajectory
    AntiGravityVisualizer.plot_trajectory(time_points, height_points)
    
    # Plot 2: Field strength
    AntiGravityVisualizer.plot_field_strength(simulator, duration=5.0)
    
    print("\n✅ Demonstration complete!")
    print("\nNext steps:")
    print("1. Run tests: python -m pytest tests/")
    print("2. Modify parameters in basic_demo.py")
    print("3. Create your own simulations!")

if __name__ == "__main__":
    main()
