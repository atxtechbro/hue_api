import React from 'react';
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';

function Scenes() {
  const triggerScene = (url) => {
    fetch(`http://localhost:5000${url}`)
      .then(response => response.text())
      .then(data => alert(data))
      .catch(error => console.error('Error:', error));
  };

  return (
    <Stack spacing={2}>
      <Button
        variant="contained"
        style={{ backgroundColor: '#FFB74D', color: 'white' }} // Soft warm orange
        onClick={() => triggerScene('/wind_down')}
      >
        Wind Down Scene
      </Button>
      <Button
        variant="contained"
        style={{ backgroundColor: '#64B5F6', color: 'white' }} // Soft calm blue
        onClick={() => triggerScene('/work_from_home')}
      >
        Work From Home Scene
      </Button>
    </Stack>
  );
}

export default Scenes;
