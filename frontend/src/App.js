import React from 'react';
import Scenes from './Scenes';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import { containerStyle, titleBoxStyle, titleTextStyle } from './styles';

function App() {
  return (
    <Container maxWidth="false" disableGutters={true} style={containerStyle}>
      <Box sx={titleBoxStyle}>
        <Typography variant="h4" component="h1" gutterBottom style={titleTextStyle}>
          Hue Lighting Demo
        </Typography>
      </Box>
      <Scenes />
    </Container>
  );
}

export default App;
