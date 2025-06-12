export type GetChatInput = {id: string}
export type SendChatInput = {
    id: string;
    message: string;
}

export type Chat = {
    id: string;
    chatsArray: Array<any>;
}