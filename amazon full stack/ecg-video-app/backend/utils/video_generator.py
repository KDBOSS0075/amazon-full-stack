class VideoGenerator:
    def __init__(self, output_path):
        self.output_path = output_path

    def generate_video(self, ecg_data):
        import numpy as np
        import matplotlib.pyplot as plt
        from matplotlib.animation import FuncAnimation

        # Create a figure and axis for the ECG plot
        fig, ax = plt.subplots()
        ax.set_title('ECG Signal')
        ax.set_xlabel('Time')
        ax.set_ylabel('Amplitude')

        # Prepare the data for the animation
        x = np.arange(len(ecg_data))
        line, = ax.plot(x, ecg_data, color='blue')

        # Update function for the animation
        def update(frame):
            line.set_ydata(ecg_data[:frame])
            return line,

        # Create the animation
        ani = FuncAnimation(fig, update, frames=len(ecg_data), blit=True)

        # Save the animation as a video file
        ani.save(self.output_path, writer='ffmpeg', fps=30)
        plt.close(fig)