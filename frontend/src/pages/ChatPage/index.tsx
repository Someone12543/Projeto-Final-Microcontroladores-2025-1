import * as React from 'react';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import { createTheme } from '@mui/material/styles';
import DashboardIcon from '@mui/icons-material/Dashboard';
import { AppProvider, type Navigation } from '@toolpad/core/AppProvider';
import { DashboardLayout } from '@toolpad/core/DashboardLayout';
import {ChatComponent} from '../../components/ChatComponent';
import {type JSX, useEffect} from "react";
import {Button, Stack} from "@mui/material";
import {ModalComponent} from "../../components/Modal";
import { ReactPhotoEditor } from 'react-photo-editor';

type Message = {
    sender: 'user' | 'printer';
    content: string | JSX.Element;
    image?: string;
    timestamp: string;
};

const demoTheme = createTheme({
    cssVariables: {
        colorSchemeSelector: 'data-toolpad-color-scheme',
    },
    colorSchemes: { light: true, dark: true },
    breakpoints: {
        values: {
            xs: 0,
            sm: 600,
            md: 600,
            lg: 1200,
            xl: 1536,
        },
    },
});

const NAVIGATION: Navigation = [
    {
        kind: 'header',
        title: 'Histórico',
    },
    {
        title: 'Chat 1',
        icon: <DashboardIcon />,
    },
];



export default function ChatPage() {
    const [log, setLog] = React.useState<Message[]>([]);
    const [imageEdit, setImageEdit] = React.useState<File>();
    const [editedImage, setEditedImage] = React.useState<File>();
    const [open, setOpen] = React.useState(false);
    const handleOpen = () => setOpen(true);
    const handleClose = () => setOpen(false);

    const [openModalEnviar, setOpenModalEnviar] = React.useState(false);
    const handleOpenModalEnviar = () => setOpenModalEnviar(true);
    const handleCloseModalEnviar = () => setOpenModalEnviar(false);
    const [imageModalEnviar, setImageModalEnviar] = React.useState<string>();

    const createFileFromPublicImage = async (imagePath: string): Promise<File> => {
        const response = await fetch(imagePath);
        const blob = await response.blob();

        // Extract filename from path
        const fileName = imagePath.split('/').pop() || 'image.jpg';

        // Create a File object from the Blob
        const file = new File([blob], fileName, { type: blob.type });
        return file;
    };

    const handleOpenModal = async (image: string)=>{
        await createFileFromPublicImage(image)
            .then(result => {
                setImageEdit(result);
                handleOpen();
            })
            .catch(error => {
                console.error(error);
            })
            .finally(() => {
            })
    }

    const handleSaveImage = async (editedFile) =>{
        handleClose();
        const url = URL.createObjectURL(editedFile);
        setImageModalEnviar(url);
        handleOpenModalEnviar();
    }

    const handleSend = async (userMessage: string) => {
        // TODO: API CALL
        const sourceImage = await createFileFromPublicImage("apple_mock.png");
        const url = URL.createObjectURL(sourceImage);

        const now = new Date().toISOString();
        setLog((prev) => [
            ...prev,
            { sender: 'user', content: userMessage, timestamp: now },
            {
                sender: 'printer',
                content: (
                    <Box>
                    <Typography>{`Recebido: "${userMessage}". Processando...`}</Typography>
                        <img src={url} style={{ width: '100%', maxWidth: '500px', borderRadius: '8px' }}/>
                    </Box>),
                timestamp: now,
            },
        ]);
    };

    return (
        <AppProvider
            navigation={NAVIGATION}
            theme={demoTheme}
            branding={{
                logo: <img alt="" />,
                title: 'IMPRESSORA BRABA :)',
                homeUrl: '/toolpad/core/introduction',
            }}
        >
            <DashboardLayout >
                <ChatComponent id={"001"} chatLog={log} onSend={handleSend} theme={demoTheme} handleOpenModal={handleOpenModal}/>
            </DashboardLayout>
            <ReactPhotoEditor
                open={open}
                onClose={handleClose}
                file={imageEdit}
                onSaveImage={handleSaveImage}
            />
            <ModalComponent open={openModalEnviar} handleClose={handleCloseModalEnviar} handleOpen={handleOpenModalEnviar} image={imageModalEnviar}/>
        </AppProvider>
    );
}