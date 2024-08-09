import React from 'react';
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';

function Scenes() {
  const triggerScene = (url) => {
    fetch(url)
      .then(response => response.text())
      .then(data => alert(data))
      .catch(error => console.error('Error:', error));
  };

  return (
    <Stack spacing={2}>
      <Button
        variant="contained"
        color="primary"
        onClick={() => triggerScene('/romantic')}
      >
        Romantic Scene
      </Button>
      <Button
        variant="contained"
        color="secondary"
        onClick={() => triggerScene('/party')}
      >
        Party Scene
      </Button>
      <Button
        variant="contained"
        color="primary"
        onClick={() => triggerScene('/stargazing')}
      >
        Stargazing Scene
      </Button>
      <Button
        variant="contained"
        color="secondary"
        onClick={() => triggerScene('/wind_down')}
      >
        Wind Down Scene
      </Button>
      <Button
        variant="contained"
        color="primary"
        onClick={() => triggerScene('/work_from_home')}
      >
        Work From Home Scene
      </Button>
      <Button
        variant="contained"
        color="secondary"
        onClick={() => triggerScene('/chill_soccer_game_night')}
      >
        Chill Soccer Game Night
      </Button>
      <Button
        variant="contained"
        color="primary"
        onClick={() => triggerScene('/colombia_goal_celebration')}
      >
        Colombia Goal Celebration
      </Button>
      <Button
        variant="contained"
        color="secondary"
        onClick={() => triggerScene('/brazil_goal_celebration')}
      >
        Brazil Goal Celebration
      </Button>
    </Stack>
  );
}

export default Scenes;
