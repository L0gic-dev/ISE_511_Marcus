import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="Plotly Animation Demo", layout="wide")

st.title("3 Basic Plotly Animations in Streamlit")

animation_choice = st.selectbox(
    "Choose an animation",
    [
        "Rotating 3D Helix",
        "Moving Sine Wave",
        "Bouncing Ball",
        "Ocean Wave"
    ],
)

num_frames = 60


def rotating_3d_helix():
    t = np.linspace(0, 8 * np.pi, 200)
    x = np.cos(t)
    z = np.sin(t)
    y = np.linspace(-2, 2, 200)

    frames = []
    for i in range(num_frames):
        angle = 2 * np.pi * i / num_frames
        x_rot = x * np.cos(angle) - z * np.sin(angle)
        z_rot = x * np.sin(angle) + z * np.cos(angle)

        frames.append(
            go.Frame(
                data=[
                    go.Scatter3d(
                        x=x_rot,
                        z=z_rot,
                        y=y,
                        mode="lines",
                    )
                ],
                name=str(i),
            )
        )

    fig = go.Figure(
        data=[
            go.Scatter3d(
                x=x,
                z=z,
                y=y,
                mode="lines",
            )
        ],
        frames=frames,
    )

    fig.update_layout(
        title="Rotating 3D Helix",
        scene=dict(
            xaxis=dict(range=[-1.5, 1.5]),
            yaxis=dict(range=[-1.5, 1.5]),
            zaxis=dict(range=[-2.5, 2.5]),
            aspectmode="cube",
        ),
        updatemenus=[
            {
                "type": "buttons",
                "buttons": [
                    {
                        "label": "Play",
                        "method": "animate",
                        "args": [
                            None,
                            {
                                "frame": {"duration": 50, "redraw": True},
                                "fromcurrent": True,
                            },
                        ],
                    },
                    {
                        "label": "Pause",
                        "method": "animate",
                        "args": [
                            [None],
                            {
                                "frame": {"duration": 0, "redraw": False},
                                "mode": "immediate",
                            },
                        ],
                    },
                ],
            }
        ],
        margin=dict(l=0, r=0, t=50, b=0),
    )
    return fig


def moving_sine_wave():
    x = np.linspace(0, 4 * np.pi, 300)

    frames = []
    for i in range(num_frames):
        phase = 2 * np.pi * i / num_frames
        y = np.sin(x + phase)

        frames.append(
            go.Frame(
                data=[
                    go.Scatter(
                        x=x,
                        y=y,
                        mode="lines",
                    )
                ],
                name=str(i),
            )
        )

    fig = go.Figure(
        data=[
            go.Scatter(
                x=x,
                y=np.sin(x),
                mode="lines",
            )
        ],
        frames=frames,
    )

    fig.update_layout(
        title="Moving Sine Wave",
        xaxis=dict(range=[0, 4 * np.pi]),
        yaxis=dict(range=[-1.5, 1.5]),
        updatemenus=[
            {
                "type": "buttons",
                "buttons": [
                    {
                        "label": "Play",
                        "method": "animate",
                        "args": [
                            None,
                            {
                                "frame": {"duration": 50, "redraw": True},
                                "fromcurrent": True,
                            },
                        ],
                    },
                    {
                        "label": "Pause",
                        "method": "animate",
                        "args": [
                            [None],
                            {
                                "frame": {"duration": 0, "redraw": False},
                                "mode": "immediate",
                            },
                        ],
                    },
                ],
            }
        ],
        margin=dict(l=0, r=0, t=50, b=0),
    )
    return fig


def bouncing_ball():
    x_positions = np.linspace(0, 10, num_frames)
    y_positions = np.abs(np.sin(np.linspace(0, 3 * np.pi, num_frames))) * 5

    frames = []
    for i in range(num_frames):
        frames.append(
            go.Frame(
                data=[
                    go.Scatter(
                        x=[x_positions[i]],
                        y=[y_positions[i]],
                        mode="markers",
                        marker=dict(size=20),
                    )
                ],
                name=str(i),
            )
        )

    fig = go.Figure(
        data=[
            go.Scatter(
                x=[x_positions[0]],
                y=[y_positions[0]],
                mode="markers",
                marker=dict(size=20),
            )
        ],
        frames=frames,
    )

    fig.update_layout(
        title="Bouncing Ball",
        xaxis=dict(range=[0, 10]),
        yaxis=dict(range=[0, 6]),
        updatemenus=[
            {
                "type": "buttons",
                "buttons": [
                    {
                        "label": "Play",
                        "method": "animate",
                        "args": [
                            None,
                            {
                                "frame": {"duration": 60, "redraw": True},
                                "fromcurrent": True,
                            },
                        ],
                    },
                    {
                        "label": "Pause",
                        "method": "animate",
                        "args": [
                            [None],
                            {
                                "frame": {"duration": 0, "redraw": False},
                                "mode": "immediate",
                            },
                        ],
                    },
                ],
            }
        ],
        margin=dict(l=0, r=0, t=50, b=0),
    )
    return fig

def generate_ocean_wave():
    # 1. Setup the grid
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x, y)

    # 2. Define the frames for the animation
    frames = []
    num_frames = 30
    
    for t in np.linspace(0, 2 * np.pi, num_frames):
        # Wave equation: Interference of two sine waves for a "rolling" effect
        Z = np.sin(X + t) * np.cos(Y + t * 0.5) + 0.5 * np.sin(X * 0.5 - t)
        
        frames.append(go.Frame(
            data=[go.Surface(z=Z, x=X, y=Y, colorscale='Viridis', showscale=False)],
            name=f'frame_{t}'
        ))

    # 3. Create the initial figure
    initial_Z = np.sin(X) * np.cos(Y) + 0.5 * np.sin(X * 0.5)
    fig = go.Figure(
        data=[go.Surface(z=initial_Z, x=X, y=Y, colorscale='Viridis', showscale=False)],
        layout=go.Layout(
            title="3D Ocean Wave Animation",
            scene=dict(
                zaxis=dict(range=[-2, 2]),
                aspectratio=dict(x=1, y=1, z=0.5)
            ),
            updatemenus=[{
                "buttons": [
                    {
                        "args": [None, {"frame": {"duration": 50, "redraw": True}, "fromcurrent": True}],
                        "label": "Play",
                        "method": "animate"
                    },
                    {
                        "args": [[None], {"frame": {"duration": 0, "redraw": True}, "mode": "immediate", "transition": {"duration": 0}}],
                        "label": "Pause",
                        "method": "animate"
                    }
                ],
                "type": "buttons",
                "direction": "left",
                "pad": {"r": 10, "t": 87},
                "showactive": False,
                "x": 0.1,
                "xanchor": "right",
                "y": 0,
                "yanchor": "top"
            }]
        ),
        frames=frames
    )
    return fig

if animation_choice == "Rotating 3D Helix":
    fig = rotating_3d_helix()
elif animation_choice == "Moving Sine Wave":
    fig = moving_sine_wave()
elif animation_choice == "Bouncing Ball":
    fig = bouncing_ball()
else:
    fig = generate_ocean_wave()

st.plotly_chart(fig, use_container_width=True)