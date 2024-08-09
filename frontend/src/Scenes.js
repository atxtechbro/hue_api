import React from 'react';
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';

function Scenes() {
  const triggerScene = (url) => {
    console.log(`Triggering scene: ${url}`); // Log the URL being triggered
    fetch(`http://localhost:5000${url}`)
      .then(response => response.text())
      .then(data => alert(data))
      .catch(error => console.error('Error:', error));
  };

  return (
    <Stack spacing={2}>
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
    </Stack>
  );
}

export default Scenes;
